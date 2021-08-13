from django.shortcuts import render
from django.shortcuts import redirect

from . import models

def index(request):
    context =  {
        # 'new_room' : None,
        'rooms' : models.Room.objects.all(),
    }
    return render(request, 'index.html', context=context)

def room(request, id = None):
    if id  == None:
        room =  models.Room.objects.create()
        return redirect('room', id=room.id)
    else:
        room =  models.Room.objects.get(id = id)

    context =  {
        # 'new_room' : None,
        'room' : room,
        'handovers' : room.handovers.all(),
    }
    return render(request, 'room.html', context=context)

def handover(request, id = None):
    if id  == None:
        handover =  models.HandingOver.objects.create()
        return redirect('handover', id=handover.id)
    else:
        handover =  models.HandingOver.objects.get(id = id)
    
    context =  {
        # 'new_room' : None,
        'handover' :handover,
        'images' : handover.images.all(),
    }
    return render(request, 'handover.html', context=context)
