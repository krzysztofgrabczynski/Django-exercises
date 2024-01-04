from django.shortcuts import redirect
from functools import wraps
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.conf import settings


def redirect_if_logged_user(func):
    """
    Decorator that checks if a user in request is logged. If user is logged it will redirect him to "home" page.
    """

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")

        return func(request, *args, **kwargs)

    return wrapper


class RedirectIfLoggedUserMixin:
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.redirect_authenticated_user()
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_field_name(self):
        redirect_field_name = (
            self.redirect_field_name or settings.SIGNUP_REDIRECT_URL
            if hasattr(settings, "SIGNUP_REDIRECT_URL")
            else self.redirect_field_name
        )

        if not redirect_field_name:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} is missing a redirect_field_name attribute. "
                f"Please define {self.__class__.__name__}.redirect_field_name or override "
                f"{self.__class__.__name__}.get_redirect_field_name()."
            )
        return str(redirect_field_name)

    def redirect_authenticated_user(self):
        return HttpResponseRedirect(self.get_redirect_field_name())
