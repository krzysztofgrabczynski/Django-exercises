from django.shortcuts import redirect
from functools import wraps


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
