from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.template import loader

from app.tasks import send_reset_password_email_task


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


class CustomPasswordResetForm(PasswordResetForm):
    """
    Custumized form class `PasswordResetForm`. Def `send_mail` changed to operate with asynchronously sending emial using celery tasks.
    """

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        message = loader.render_to_string(email_template_name, context)

        send_reset_password_email_task.delay(message, from_email, to_email)
