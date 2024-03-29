from django.urls import path
from django.contrib.auth import views as auth_views

from app import views as app_views


urlpatterns = [
    path("home/", app_views.HomeView.as_view(), name="home"),
    path("sign-up/", app_views.CreateUserFormView.as_view(), name="sign_up"),
    path("login/", app_views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "forget_password/",
        app_views.ForgetPasswordView.as_view(),
        name="forget_password",
    ),
    path(
        "reset_password/<uidb64>/<token>/",
        app_views.CustomPasswordResetConfirmView.as_view(),
        name="reset_password",
    ),
    path(
        "new_trip_idea/", app_views.CreateTripIdeaView.as_view(), name="new_trip_idea"
    ),
    path("detail_trip/<pk>/", app_views.TripDetailView.as_view(), name="detail_trip"),
    path(
        "update_trip_idea/<pk>/",
        app_views.UpdateTripIdeaView.as_view(),
        name="update_trip_idea",
    ),
    path(
        "delete_trip_idea/<pk>/",
        app_views.DeleteTripIdeaView.as_view(),
        name="delete_trip_idea",
    ),
]
