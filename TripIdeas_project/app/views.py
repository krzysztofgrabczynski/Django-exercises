from typing import Any
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView,
    LoginView,
)

from app.forms import UserRegistrationForm, CustomPasswordResetForm, CreateTripIdeaForm
from app.models import UserProfile, TripModel
from core.settings import EMAIL_HOST_USER


def home(request):
    return HttpResponse("home page")


class CustomLoginView(LoginView):
    redirect_authenticated_user = True


class CreateUserFormView(generic.FormView):
    template_name = "registration/sign_up.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        phone_number = form.cleaned_data["phone_number"]

        UserProfile.objects.create(user=user, phone_number=phone_number)
        login(self.request, user)

        return super().form_valid(form)


class ForgetPasswordView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = "registration/forget_password.html"
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy("login")
    email_template_name = "registration/email_template_name.html"
    from_email = EMAIL_HOST_USER


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "registration/reset_password.html"
    success_url = reverse_lazy("login")


class CreateTripIdeaView(generic.edit.CreateView):
    model = TripModel
    form_class = CreateTripIdeaForm
    success_url = reverse_lazy("home")
    template_name = "create_trip_idea.html"

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs
