from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, "climbed/index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = UserCreationForm()
    return render(request, "climbed/register.html", {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")

    return render(request, {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
