from django.shortcuts import render
from django.views import View

from oddam_w_dobre_rece.models import Donation, Institution


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


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class ConfrimDonation(View):
    def get(self, request):
        return render(request, "form-confirmation.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")
