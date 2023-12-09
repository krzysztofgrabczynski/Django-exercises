from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.views import PasswordResetView

from app.forms import UserRegistrationForm, CustomPasswordResetForm
from app.models import UserProfile
from core.settings import EMAIL_HOST_USER


def home(request):
    return HttpResponse("home page")


class CreateUserFormView(generic.FormView):
    template_name = "registration/sign_up.html"
    form_class = UserRegistrationForm
    success_url = "home/"

    def form_valid(self, form):
        user = form.save()
        phone_number = form.cleaned_data["phone_number"]

        UserProfile.objects.create(user=user, phone_number=phone_number)
        login(self.request, user)

        return super().form_valid(form)


class ForgetPasswordView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = "registration/forget_password.html"
    success_url = "/app/login/"
    email_template_name = "registration/email_template_name.html"
    from_email = EMAIL_HOST_USER
