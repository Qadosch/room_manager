from django.db import models
from django.db.models.deletion import CASCADE

class Room(models.Model):
    name = models.CharField(blank=True, max_length=256)
    renter = models.CharField(blank=True, max_length=256)
    img = models.FileField()

class HandingOver(models.Model):
    date = models.DateField()

    room = models.ForeignKey(Room, models.SET_NULL, blank=True, null=True,)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Image(models.Model):
    img = models.FileField()

    handing_over = models.ForeignKey(HandingOver, models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
