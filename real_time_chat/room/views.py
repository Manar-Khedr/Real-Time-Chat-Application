from django.shortcuts import render,redirect
from .models import Room, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#make sure that the user is authenticated
@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room= Room.objects.get(slug=slug)
    messages= Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})

def get_user_list():
    users = User.objects.all()
    # If you have a user profile model:
    # user_profiles = UserProfile.objects.all()
    return users
    