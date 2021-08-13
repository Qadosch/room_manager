"""room_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.room, name='room'),
    path('room/<int:room_id>/', views.room, name='room'),
    path('room/<int:room_id>/handover/', views.handover, name='handover'),
    path('room/<int:room_id>/handover/<int:handover_id>/', views.handover, name='handover'),
    # path('handover/<int:id>/edit/', views.handover, name='handover'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
