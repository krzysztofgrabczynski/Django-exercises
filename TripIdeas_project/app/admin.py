from django.contrib import admin

from app.models import UserProfile, PriceModelWithTracker, TripModel


admin.site.register(UserProfile)
admin.site.register(PriceModelWithTracker)
admin.site.register(TripModel)
