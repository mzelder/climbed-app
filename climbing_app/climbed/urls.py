from django.urls import path
from climbed import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view")
]