from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("time/", views.time_measure, name='time_measure'),
]