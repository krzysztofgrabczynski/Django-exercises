from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.template import loader

from app.tasks import send_reset_password_email_task
from app.models import TripModel, PriceModelWithTracker, UserProfile


class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "phone_number"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        sandard_number_length = 9
        if not phone_number.isdigit() or not len(phone_number) == sandard_number_length:
            raise forms.ValidationError("Phone number must be a number with 9 digits")

        return phone_number

    def save(self):
        user = super().save()
        phone_number = self.cleaned_data["phone_number"]
        UserProfile.objects.create(user=user, phone_number=phone_number)

        return user


class CustomPasswordResetForm(PasswordResetForm):
    """
    Custumized `PasswordResetForm` class. Changed `send_mail` method to work with celery and redis (asynchronous email sending).
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


class CreateTripIdeaForm(forms.ModelForm):
    clean_price = forms.FloatField(label="Price")

    class Meta:
        model = TripModel
        fields = [
            "owner",
            "name",
            "destination",
            "description",
            "clean_price",
            "is_abroad",
            "contact_number",
        ]
        widgets = {"owner": forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self._set_current_user(current_user)

    def _set_current_user(self, user):
        if user is not None:
            self.initial["owner"] = user
        else:
            raise forms.ValidationError(
                "Class %s requires the 'user' keyword argument in the "
                "get_form_kwargs method. Please override the 'get_form_kwargs' method in the "
                "view that calls this class and include 'user' as 'request.user'."
                % self.__class__.__name__
            )

    def clean_contact_number(self):
        contact_number = self.cleaned_data["contact_number"]
        sandard_number_length = 9
        if (
            not contact_number.isdigit()
            or not len(contact_number) == sandard_number_length
        ):
            raise forms.ValidationError("Contact number is not a valid number")
        return contact_number

    def save(self, *args, **kwargs):
        price = self.cleaned_data["clean_price"]
        self.instance.price = PriceModelWithTracker.objects.create(price=price)
        return super().save(*args, **kwargs)
