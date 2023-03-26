from django.shortcuts import render, HttpResponse, redirect
from .models import BaseModel
from .forms import AddNewForm


def index(request):
    objects = BaseModel.get_all_objects()

    context = {
        'objects': objects
    }
    return render(request, 'index.html', context)

def create_film(request):
    form = AddNewForm(request.POST or None)

    if request.method == 'POST':
        pass

    return render(request, 'create_obj.html', {'form': form})

def create_book(request):
    form = AddNewForm(request.POST or None)

    if request.method == 'POST':
        pass

    return render(request, 'create_obj.html', {'form': form})

def create_article(request):
    form = AddNewForm(request.POST or None)

    if request.method == 'POST':
        pass

    return render(request, 'create_obj.html', {'form': form})