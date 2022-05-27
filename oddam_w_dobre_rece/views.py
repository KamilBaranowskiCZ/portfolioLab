from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from oddam_w_dobre_rece.models import Category, Donation, Institution
from .forms import RegisterForm, DonationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user

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
        fundations = Institution.objects.filter(type='Foundation')
        non_governmental_organization = Institution.objects.filter(type='Non-governmental organization')
        local_collection = Institution.objects.filter(type='Local collection')
        return render(
            request,
            "index.html",
            {
                "sum_of_donations": sum_of_donations,
                "sum_of_supported_institution": sum_of_supported_institution,
                "fundations": fundations,
                "non_governmental_organization": non_governmental_organization,
                "local_collection": local_collection,
            },
        )


class AddDonation(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        name = get_user(self.request)
        donation_form = DonationForm(
            initial={"user": name})
        return render(request, "form.html", {"categories": categories, "institutions": institutions, "donation_form": donation_form})


class ConfrimDonation(View):
    def get(self, request):
        return render(request, "form-confirmation.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")
