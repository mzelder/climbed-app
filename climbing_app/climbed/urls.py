from django.urls import path
from climbed import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_month/<str:action>/<int:current_month>/<int:current_year>", views.get_month, name="get_month"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login_view"),
    path("logout_view", views.logout_view, name="logout_view"),
    path("add_workout", views.add_workout, name="add_workout")
]