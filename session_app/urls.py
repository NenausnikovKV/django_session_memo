from django.urls import path
from . import views

app_name = "session_app"

urlpatterns = [
    path("", views.index),
]
