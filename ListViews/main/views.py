from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

