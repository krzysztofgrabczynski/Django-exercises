from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import login

from app.forms import UserRegistrationForm, ForgetPasswordForm
from app.models import UserProfile
from app.tasks import send_reset_password_email_task


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


class ForgetPasswordView(generic.FormView):
    template_name = "registration/forget_password.html"
    form_class = ForgetPasswordForm
    success_url = "/app/login/"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        reset_password_link = ...

        send_reset_password_email_task.delay(reset_password_link, email)

        return super().form_valid(form)
    
