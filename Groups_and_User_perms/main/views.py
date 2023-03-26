from django.shortcuts import render, HttpResponse, redirect
from .models import BaseModel


def index(request):
    objects = BaseModel.get_all_objects()

    context = {
        'objects': objects
    }
    return render(request, 'index.html', context)
