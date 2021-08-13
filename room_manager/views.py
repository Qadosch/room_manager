from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context =  {
        # 'new_room' : None,
        'rooms' : models.Room.objects.all(),
    }
    return render(request, 'index.html', context=context)


@login_required
def room(request, room_id = None):
    if not request.user.is_authenticated:
        return redirect('login')
    if room_id  == None:
        room =  models.Room.objects.create()
        return redirect('room', room_id=room.id)
    else:
        room =  models.Room.objects.get(id = room_id)
    
    if request.method == 'POST':
        form = forms.RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room.name = form.cleaned_data['name']
            room.description = form.cleaned_data['description']
            room.person = form.cleaned_data['person']
            if form.cleaned_data['img']:
                room.img = form.cleaned_data['img']

            room.save()



    context =  {
        # 'new_room' : None,
        'room' : room,
        'handovers' : room.handovers.all(),
    }
    return render(request, 'room.html', context=context)

@login_required
def handover(request, room_id,  handover_id=None):

    if handover_id  == None:
        room =  models.Room.objects.get(id = room_id)
        handover =  models.HandingOver.objects.create(room=room)
        return redirect('handover',room_id=room_id, handover_id=handover.id)
    else:
        handover =  models.HandingOver.objects.get(id = handover_id)
    
    if request.method == 'POST':
        form = forms.HandingOverForm(request.POST, request.FILES)
        if form.is_valid():
            handover.description = form.cleaned_data['description']
            handover.person = form.cleaned_data['person']
            handover.date = form.cleaned_data['date']
            handover.save()
    
    if request.method == 'POST':
        handover =  models.HandingOver.objects.get(id = handover_id)
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("valiiiiid slave")
            if form.cleaned_data['immage_id']:
                img = models.Image.objects.get(id=form.cleaned_data['immage_id'])
            else:
                img = models.Image.objects.create(handing_over=handover)

            img.description = form.cleaned_data['immage_description']
            if form.cleaned_data['immage_img']:
                img.img = form.cleaned_data['immage_img']

            img.save()
    
    context =  {
        # 'new_room' : None,
        'handover' :handover,
        'images' : handover.images.all(),
    }
    return render(request, 'handover.html', context=context)
