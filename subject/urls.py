from django.urls import path
from . import views

urlpatterns = [
    path("", views.subject_main, name='subject_main_view'),
    path("delete/", views.subject_delete),
    path("add/", views.subject_add, name='subject_add_view'),
    path("category/", views.category_manage, name='category_manage_view'),
    path("time/", views.time_measure, name='time_measure'),
]