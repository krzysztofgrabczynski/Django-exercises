from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(null=False, blank=False, max_length=9)

class FloatFieldWithTracking(models.FloatField):
    def __init__(self, track_attribute_name: str, *args: Any, **kwargs: Any) -> None:
        self._name = None
        self.track_attribute_name = track_attribute_name
        super().__init__(*args, **kwargs)

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        expanded_value = self.add_datetime_to_value(value)
        if not hasattr(instance, self.track_attribute_name):
            instance.__dict__[self.track_attribute_name] = [expanded_value]
        else:
            instance.__dict__[self.track_attribute_name].append(expanded_value)
        
        instance.__dict__[self._name] = value

    def add_datetime_to_value(self, value):
        return (value, datetime.now())


class TripModel(models.Model):
    owner = ...
    name = ...
    destination = ...
    description = ...
    price = ...
    is_abroad = ...
    contact_number = ...
    

    
