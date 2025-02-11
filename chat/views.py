# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('chat')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_view(request, username=None):
    # List all users except the logged-in user:
    users = User.objects.exclude(username=request.user.username)
    chat_partner = None
    messages = []
    if username:
        try:
            chat_partner = User.objects.get(username=username)
            messages = ChatMessage.objects.filter(
                Q(sender=request.user, receiver=chat_partner) |
                Q(sender=chat_partner, receiver=request.user)
            )
        except User.DoesNotExist:
            chat_partner = None
    context = {
        'users': users,
        'chat_partner': chat_partner,
        'messages': messages
    }
    return render(request, 'chat/chat.html', context)
