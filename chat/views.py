from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Message

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

@login_required
def chat(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/chat.html', {'users': users})

@login_required
def room(request, room_name):
    other_user = User.objects.get(username=room_name)
    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(receiver=other_user)) |
        (models.Q(sender=other_user) & models.Q(receiver=request.user))
    ).order_by('timestamp')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'other_user': other_user,
        'messages': messages
    })