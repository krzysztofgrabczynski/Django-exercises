from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(null=False, blank=False, max_length=9)


class FloatFieldWithTracking(models.FloatField):
    """
    Descriptor class.
    Customized `models.FloatField` class with tracking functionality to store all modified values in given in `track_attribute_name` attribute.
    """
    
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

    def values_between_dates(self, start: datetime, end: datetime) -> list:
        values = self.__dict__[self.track_attribute_name]
        return [x for x in values if start < x < end]
    

class TripModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    destination = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(default="")
    price = FloatFieldWithTracking(track_attribute_name="trip_price_history", null=False, blank=False)
    is_abroad = models.BooleanField(null=False, blank=False)
    contact_number = models.CharField(max_length=9, null=False, blank=False)
    
    def min_price_between_dates(self, start:datetime, end:datetime):
        return min(self.price.values_between_dates(start, end))
            
    def get_last_price(self):
        return self.price.track_attribute_name[-2]
    