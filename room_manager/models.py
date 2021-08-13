from django.db import models
from django.db.models.deletion import CASCADE

class Room(models.Model):
    name = models.CharField(blank=True, max_length=256)
    description = models.TextField()
    img = models.ImageField()
    person = models.CharField(blank=True, max_length=256)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class HandingOver(models.Model):
    room = models.ForeignKey(Room, related_name='handovers', on_delete=models.SET_NULL, blank=True, null=True,)

    date = models.DateField(blank=True, null=True)
    person = models.CharField(blank=True, max_length=256)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Image(models.Model):
    handing_over = models.ForeignKey(HandingOver, related_name='images', on_delete=models.CASCADE)

    img = models.ImageField()
    description = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
