from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
    return render(request, "index.html")

def checkroom(request):
    room_name = request.POST["room_name"]
    username = request.POST["username"]
    if Room.objects.filter(room_name = room_name).exists():
        return redirect("/" + room_name + "/?username=" + username)
    else:
        new_room = Room.objects.create(room_name=room_name)
        new_room.save()
        return redirect("/" + room_name + "/?username=" + username)

def room(request, room_name):
    username = request.GET.get("username")
    return render(request, "room.html", {
        "room_name" : room_name,
        "username" : username
    })

def send(request):
    username = request.POST["username"]
    value = request.POST["message"]
    room_name = request.POST["room_name"]
    new_mes = Message.objects.create(username=username, value=value)
    new_mes.save()
    new_mes.room.add(Room.objects.filter(room_name=room_name)[0])
    return HttpResponse("successfully")

def getmessages(request, room_name):
    messages = Message.objects.filter(room= Room.objects.filter(room_name=room_name)[0])
    return JsonResponse({
        "messages" : list(messages.values())
    })