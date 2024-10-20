from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    return render(request, "climbed/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "climbed/login.html", {
                "message": "Invalid name and/or username",
                "status": "error"
            })
    else:
        return render(request, "climbed/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        
        if password != confirmation:
            return render(request, "climbed/register.html", {
                "message": "Passwords must match.",
                "status": "error"
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "climbed/register.html", {
                "message": "Username already taken.",
                "status": "error"
            })
        login(request, user)
        return redirect("index")
    else:
        return render(request, "climbed/register.html")