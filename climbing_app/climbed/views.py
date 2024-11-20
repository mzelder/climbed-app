import calendar
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from .models import Workout
from .helpers import get_month_informations


def index(request):
    if request.user.is_authenticated:
        now = timezone.localtime(timezone.now())
        date = get_month_informations(now.month, now.year)
        return render(request, "climbed/index.html", {"date": date})
    else:   
        return render(request, "climbed/index.html")

def get_month(request, action, current_month, current_year):
    if action == "previous":
        date = get_month_informations(current_month - 1, current_year)
    elif action == "next":
        date = get_month_informations(current_month + 1, current_year)
    
    return JsonResponse(date)

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
    
def add_workout(request):
    if request.method == "POST":
        # Data from showForm() in script.js 
        title = request.POST["workout_title"]
        type = request.POST["workout_type"]
        planned_tiredness = request.POST["planned_tiredness"]
        date = request.POST["date"]
        description = request.POST["workout_description"]

        workout = Workout.objects.create(
            title=title,
            workout_type=type,
            planned_tiredness=planned_tiredness,
            date=date,
            workout_description=description,
            user=request.user
        )
        workout.save()
        workouts = Workout.objects.all()
        for workout in workouts: 
            print(workout.title, workout.date)
            print()

    
    return redirect("index")
