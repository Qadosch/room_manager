from django.shortcuts import render
from django.shortcuts import redirect

from . import models

def index(request):
    context =  {
        # 'new_room' : None,
        'rooms' : models.Room.objects.all(),
    }
    return render(request, 'index.html', context=context)

def room(request, room_id = None):
    if room_id  == None:
        room =  models.Room.objects.create()
        return redirect('room', room_id=room.id)
    else:
        room =  models.Room.objects.get(id = room_id)

    context =  {
        # 'new_room' : None,
        'room' : room,
        'handovers' : room.handovers.all(),
    }
    return render(request, 'room.html', context=context)

def handover(request, room_id,  handover_id=None):
    if handover_id  == None:
        room =  models.Room.objects.get(id = room_id)
        handover =  models.HandingOver.objects.create(room=room)
        return redirect('handover',room_id=room_id, handover_id=handover.id)
    else:
        handover =  models.HandingOver.objects.get(id = handover_id)
    
    context =  {
        # 'new_room' : None,
        'handover' :handover,
        'images' : handover.images.all(),
    }
    return render(request, 'handover.html', context=context)
