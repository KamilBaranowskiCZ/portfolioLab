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
from oddam_w_dobre_rece.views import LandingPage, AddDonation, Login, Register, ConfrimDonation, register
from oddam_w_dobre_rece.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", LandingPage.as_view(), name="index"),
    path("form/", AddDonation.as_view(), name="adddonation"),
    path("form-confirm/", ConfrimDonation.as_view(), name="confirmdonation"),
    re_path(r'^login/$',auth_views.LoginView.as_view(template_name='login.html',authentication_form=UserLoginForm
            ),name='login'),
    path("", include("django.contrib.auth.urls")),
    path("register/", register , name="register"),
]
