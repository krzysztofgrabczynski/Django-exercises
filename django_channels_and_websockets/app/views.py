from django.shortcuts import render, redirect   
from django.http import Http404
import uuid

from .forms import ImageLink
from .tasks import download_image as download_image_task

def home(request):
    return render(request, "home.html")

def chat(request, room_name: str):
    chat_rooms = [
        "room1",
        "room2",
    ]
    if room_name in chat_rooms:
        return render(request, "chat.html", {"room_name": room_name})
    raise Http404("Room not found")

def download_image(request):
    form = ImageLink(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data["url"]
        client_uuid = str(uuid.uuid4())
        download_image_task.delay(url, client_uuid)
        return render(request, "download_image.html", {"form": form, "client_uuid": client_uuid})
    return render(request, "download_image.html", {"form": form})