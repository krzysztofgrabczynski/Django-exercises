from django.contrib import admin

from shop.models import TestOrder, TestProduct


admin.site.register(TestOrder)
admin.site.register(TestProduct)
