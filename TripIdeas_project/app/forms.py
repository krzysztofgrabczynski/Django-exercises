from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit() or not len(phone_number) == 9:
            raise forms.ValidationError("Phone number must be a number with 9 digits")

        return phone_number


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address does not exist")
        
        return email
