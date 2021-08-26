from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("checkroom", views.checkroom, name = "checkview"),
    path("<str:room_name>/", views.room, name = "room"),
    path("send", views.send, name = "send"),
    path("getmessages/<str:room_name>/", views.getmessages, name = "getmessages")
]