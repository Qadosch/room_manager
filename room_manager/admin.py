from django.contrib import admin
from . import models

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'person']

@admin.register(models.HandingOver)
class HandingOverAdmin(admin.ModelAdmin):
    list_display = ['date', 'person', 'description']
