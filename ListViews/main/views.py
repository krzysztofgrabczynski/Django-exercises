from django.shortcuts import render
from django.views.generic import ListView
from datetime import datetime

from .models import Product


class ProductView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        name_filter = self.request.GET.get('filter', '') 
        if name_filter:
            return queryset.filter(name__icontains=name_filter)
        else:
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.now()
        return context