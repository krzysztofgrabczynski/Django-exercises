from django.views import generic
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login
from django.core.signing import dumps, loads
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.template import loader

from app.forms import UserRegistrationForm, ForgetPasswordForm
from app.models import UserProfile
from app.tasks import send_reset_password_email_task
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


# class ForgetPasswordView(generic.FormView):
#     template_name = "registration/forget_password.html"
#     form_class = ForgetPasswordForm
#     success_url = "/app/login/"

#     def form_valid(self, form):
#         email = form.cleaned_data["email"]
#         user = User.objects.get(email=email)
#         reset_password_link = reverse("reset_password", kwargs={"hash_user_id":dumps(user.id)})
#         print(reset_password_link)
#         # send_reset_password_email_task.delay(reset_password_link, email)

#         return super().form_valid(form)

class ForgetPasswordView(PasswordResetView):
    template_name = "registration/forget_password.html"
    form_class = ForgetPasswordForm
    success_url = "/app/login/"
    email_template_name = "registration/email_template_name.html"
    from_email = EMAIL_HOST_USER

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

        send_reset_password_email_task.delay()


    
