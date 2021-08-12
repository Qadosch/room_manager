from django.db import models
from django.db.models.deletion import CASCADE

class Room(models.Model):
    name = models.CharField(blank=True, max_length=256)
    description = models.TextField()
    img = models.FileField()
    person = models.CharField(blank=True, max_length=256)


class HandingOver(models.Model):
    room = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True,)

    date = models.DateField()
    person = models.CharField(blank=True, max_length=256)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Image(models.Model):
    handing_over = models.ForeignKey(HandingOver, models.CASCADE)

    img = models.FileField()
    description = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
