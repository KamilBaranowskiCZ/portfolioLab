from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from oddam_w_dobre_rece.models import Category, Donation, Institution
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/login")
            except:
                messages.error(request,"Użytkownik o podanym Emailu istnieje!")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
    
    


class LandingPage(View):
    def get(self, request):
        sum_of_donations = Donation.objects.count()
        sum_of_supported_institution = (
            Donation.objects.values_list("institution_id", flat=True)
            .distinct()
            .count()
        )
        fundations = Institution.objects.filter(type='Foundation').order_by("pk")
        p = Paginator(fundations, 5)
        page = request.GET.get('page')
        all_foundations = p.get_page(page)
        non_governmental_organization = Institution.objects.filter(type='Non-governmental organization').order_by("pk")
        p = Paginator(non_governmental_organization, 5)
        page = request.GET.get('page')
        all_non_governmental_organization = p.get_page(page)
        local_collection = Institution.objects.filter(type='Local collection').order_by("pk")
        p = Paginator(local_collection, 5)
        page = request.GET.get('page')
        all_local_collection = p.get_page(page)
        return render(
            request,
            "index.html",
            {
                "sum_of_donations": sum_of_donations,
                "sum_of_supported_institution": sum_of_supported_institution,
                "all_non_governmental_organization": all_non_governmental_organization,
                "all_local_collection": all_local_collection,
                "all_foundations": all_foundations
            },
        )


class AddDonation(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, "form.html", {"categories": categories, "institutions": institutions})


class ConfrimDonation(View):
    def post(self, request):
        donation = Donation.objects.create(
                quantity=request.POST["bags"],
                institution=Institution.objects.get(id=request.POST["organization"]),
                address=request.POST["address"],
                phone_number=request.POST["phone"],
                city=request.POST["city"],
                zip_code=request.POST["postcode"],
                pick_up_date=request.POST["data"],
                pick_up_time=request.POST["time"],
                pick_up_comment=request.POST["more_info"],
                user=get_user(self.request)
            )
        categories = request.POST.getlist("categories")
        for category in categories:          
            donation.categories.add(category)
        donation.save()
        return render(request, "form-confirmation.html")


class UserDetails(View):
    def get(self, request):
        return render(request, "user_details.html")


class UserDonations(View):
    def get(self, request):
        userID = get_user(self.request).id
        donations = Donation.objects.filter(user_id=userID).order_by("is_taken","pick_up_date","pk")
        return render(request, "user_donations.html",{"donations": donations})

class PickUpDonation(View):
    def get(self, request, donation_id):
        donation = Donation.objects.get(id=donation_id)
        donation.is_taken = True
        donation.taken_date = datetime.now()
        donation.save()
        return redirect("userdonations")

class CancelPickUpDonation(View):
    def get(self, request, donation_id):
        donation = Donation.objects.get(id=donation_id)
        donation.is_taken = False
        donation.taken_date = None
        donation.save()
        return redirect("userdonations")

class UserProfileEdit(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, "edit_user_profile.html", context={"user": user})
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        if not first_name:
            return render(request, "edit_user_profile.html", context={"error": "Podaj imię"})
        if not last_name:
            return render(request, "edit_user_profile.html", context={"error": "Podaj nazwisko"})
        if not username:
            return render(request, "edit_user_profile.html", context={"error": "Podaj email"})
        try:
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.save()
        except:
            return render(request, "edit_user_profile.html", context={"error": "Użytkownik o podanym mailu już istnieje "})
        return redirect("/")