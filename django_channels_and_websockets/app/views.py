from django.shortcuts import render
from django.http import Http404


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
