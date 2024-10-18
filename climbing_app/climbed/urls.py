from django.urls import path
from climbed import views

urlpatterns = [
    path("", views.index, name="home")
]