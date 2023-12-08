from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

from app import views as app_views
from app.mixins import if_logged_user


urlpatterns = [
    path("home/", app_views.home, name="home"),
    path("sign-up/", app_views.CreateUserFormView.as_view(), name="sign_up"),
    path("login/", if_logged_user(LoginView.as_view()), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("forget_passowrd/", app_views.ForgetPasswordView.as_view(), name="forget_passowrd"),
    path("reset_password/<str:hash_user_id>/", PasswordResetView.as_view(), name="reset_password"),
]
 