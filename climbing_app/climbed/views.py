from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, "climbed/index.html")

def login_view(request):
    # if request.method == "POST":
        #user = authenticate(username=username, password=password)
        # if user:
        #     login(request, user)
        #     return redirect("index")

    return render(request, "climbed/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = UserCreationForm()
    return render(request, "climbed/register.html", {'form': form})
