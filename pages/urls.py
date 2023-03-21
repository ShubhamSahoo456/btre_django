from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name="index"),
    path('about', view=views.about, name="about")
]
