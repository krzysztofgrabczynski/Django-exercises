from django.shortcuts import render
from django.http.response import HttpResponse

from .tasks import add


def home(request):
    add.delay(2, 2)
    return HttpResponse("Done")
