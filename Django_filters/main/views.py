from django.shortcuts import render
from .models import Film


def index(request, *args, **kwargs):
    films = Film.objects.all()
    
    context = {
        'films': films
    }
    return render(request, 'index.html', context)
