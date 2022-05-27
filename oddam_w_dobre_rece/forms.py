from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import Donation


# Create your forms here.


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"placeholder": "Imię"})
        self.fields["last_name"].widget.attrs.update(
            {"placeholder": "Nazwisko"}
        )
        self.fields["email"].widget.attrs.update({"placeholder": "Email"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Hasło"})
        self.fields["password2"].widget.attrs.update(
            {"placeholder": "Powtórz hasło"}
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = "{}".format(
            self.cleaned_data["email"],
        )
        if commit:
            user.save()
        return user


from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Hasło",
            }
        )
    )


class DonationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True

    class Meta:
        fields = (
            "quantity",
            "categories",
            "institution",
            "address",
            "phone_number",
            "city",
            "zip_code",
            "pick_up_date",
            "pick_up_time",
            "pick_up_comment",
            "user",
        )
        model = Donation
