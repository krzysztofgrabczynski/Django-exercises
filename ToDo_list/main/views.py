from django.shortcuts import render, HttpResponse
from .models import Goal, GoalsList

def home(request):
    return HttpResponse('home')

def undo(request):
    return HttpResponse('undo')

def redo(request):
    return HttpResponse('redo')

def save(request):
    return HttpResponse('save')



