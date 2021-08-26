from django.db import models
import datetime

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    username = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(default= datetime.datetime.now(), blank=True)
    room = models.ManyToManyField(Room)