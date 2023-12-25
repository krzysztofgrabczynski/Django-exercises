from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from field_history.tracker import FieldHistoryTracker


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(null=False, blank=False, max_length=9)


class PriceModelWithTracker(models.Model):
    price = models.FloatField(null=True, blank=False)
    price_history = FieldHistoryTracker(["price"])

    def __str__(self):
        return str(self.price)

    def __repr__(self):
        return self.__str__()

    def min_price_between_dates(self, start: datetime.date, end: datetime.date):
        try:
            return min(
                (
                    x.field_value
                    for x in self.price_history.all()
                    if start <= x.date_created.date() <= end
                )
            )
        except ValueError as e:
            raise ValueError(
                "Probably there is no prices between provided dates. Raises: %s" % e
            )
        except TypeError:
            raise TypeError(
                "Error in `min_price_between_dates` method: `start` or `end` value are not `datetime.date` type."
            )

    def get_price_before_change(self):
        if self.price_history.count() > 1:
            queryset = self.price_history.all().order_by("-date_created")
            return queryset[1].field_value
        else:
            raise ValueError("There is only one price for %s trip" % self.name)


class TripModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=128, null=False, blank=False)
    destination = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(default="")
    price = models.OneToOneField(PriceModelWithTracker, on_delete=models.CASCADE)
    is_abroad = models.BooleanField(null=False, blank=False)
    contact_number = models.CharField(max_length=9, null=False, blank=False)
