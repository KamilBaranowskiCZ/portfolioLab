"""portfolioLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from oddam_w_dobre_rece.views import (
    LandingPage,
    AddDonation,
    ConfrimDonation,
    register,
    UserDetails,
    UserDonations,
    PickUpDonation,
    CancelPickUpDonation,
    UserProfileEdit,
)
from oddam_w_dobre_rece.forms import UserLoginForm,PasswordChangeForm


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LandingPage.as_view(), name="index"),
    path("form/", AddDonation.as_view(), name="adddonation"),
    path("form-confirm/", ConfrimDonation.as_view(), name="confirmdonation"),
    re_path(
        r"^login/$",
        auth_views.LoginView.as_view(
            template_name="login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
        re_path(
        r"^change_password/$",
        auth_views.PasswordChangeView.as_view(
            template_name="change_password.html",form_class=PasswordChangeForm, success_url = '/'
        ),
        name="change_password",
    ),
    path("", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path("user_details/", UserDetails.as_view(), name="userdetails"),
    path("user_donations/", UserDonations.as_view(), name="userdonations"),
    path(
        "user_donations/pickup/<int:donation_id>/",
        PickUpDonation.as_view(),
        name="pickupdonation",
    ),
        path(
        "user_donations/cancelpickup/<int:donation_id>/",
        CancelPickUpDonation.as_view(),
        name="cancelpickupdonation",
    ),
    path("user_details/<int:user_id>/", UserProfileEdit.as_view(), name="edituserdetails"),
]
