from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import login

from app.forms import UserRegistrationForm
from app.models import UserProfile


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
    
        return super().form_valid(form)