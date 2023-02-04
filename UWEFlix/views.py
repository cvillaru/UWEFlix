from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return HttpResponse('Hello Django')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("there was an error logging in, please try again"))
            return redirect('login')
    else:
        return render(request, 'UWEFlix/login.html', {})