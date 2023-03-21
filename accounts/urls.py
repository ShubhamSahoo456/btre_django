from django.urls import path
from . import views

urlpatterns = [
    path("register",view=views.register,name="register"),
    path("login",view=views.login,name="login"),
    path("logout",view=views.logout,name="logout"),
    path("dashboard",view=views.dashboard,name="dashboard")
]