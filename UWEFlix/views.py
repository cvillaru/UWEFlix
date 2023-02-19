from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    
    name = "UWEFlix"

    return render(request, 'UWEFlix/home.html', {
        'name': name
    })


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
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
        else: 
            messages.success(request, ("There was an error creating an account, please try again"))
            return redirect(request, 'home')
    else:
        form = UserCreationForm()
    return render(request, 'UWEFlix/register_user.html', {'form': form})