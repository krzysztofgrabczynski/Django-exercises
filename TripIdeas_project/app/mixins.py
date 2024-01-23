from django.shortcuts import redirect
from functools import wraps
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.mixins import AccessMixin


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


class ObjectOwnerRequiredMixin(AccessMixin):
    permission_denied_message = (
        "You have to be the owner of the object you are trying to delete."
    )
    owner_field_name = None

    def _get_object_owner(self):
        assert self.owner_field_name is not None, (
            f"`ObjectOwnerRequiredMixin.owner_field_name` cannot be None."
            f"You must override `ObjectOwnerRequiredMixin.owner_field_name` in {self.__class__.__name__} class."
        )

        fields = [field.name for field in self.model._meta.fields]
        if not self.owner_field_name in fields:
            raise ImproperlyConfigured(
                f"{self.model} needs to define `{self.owner_field_name}` field."
            )

        return getattr(self.get_object(), self.owner_field_name)

    def dispatch(self, request, *args, **kwargs):
        if not request.user == self._get_object_owner():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class RecentlyViewedItemsMixin:
    model = None
    atribute_field_name = "recently_viewed_items"

    def get(self, request, *args, **kwargs):
        self._add_item_to_viewed_list(self.get_object())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recently_viewed_items = self.request.session[self.atribute_field_name]
        context = self._add_to_context(recently_viewed_items, context)

        return context

    def get_model(self):
        if self.model is None:
            raise ImproperlyConfigured(
                f"You must provide a model field in {self.__class__.__name__} class."
            )
        return self.model

    @property
    def recently_viewed_items(self):
        return self.request.session.get(self.atribute_field_name, [])

    def _add_item_to_viewed_list(self, obj):
        object_list = self.recently_viewed_items
        object_list_max_len = 5

        if object_list == []:
            self._add_first_obj(object_list, obj)
        else:
            if obj.id in object_list:
                object_list.remove(obj.id)

            if len(object_list) == object_list_max_len:
                object_list.pop()

            object_list.insert(0, obj.id)

        self.request.session[self.atribute_field_name] = object_list

    def _add_first_obj(self, obj_list, obj):
        obj_list.insert(0, obj.id)

    def _add_to_context(self, items_list, context):
        objects_from_items_list = self.get_model().objects.filter(pk__in=items_list)
        sorted_objects = sorted(
            objects_from_items_list, key=lambda x: items_list.index(x.id)
        )

        context.update({self.atribute_field_name: sorted_objects})

        return context
