from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Workout(models.Model):
    title = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=100)
    planned_tiredness = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)]
    )
    date = models.DateTimeField()
    workout_description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class AfterWorkout(models.Model):
    tiredness = models.IntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)]
    )
    feeling_description = models.CharField(max_length=1000)