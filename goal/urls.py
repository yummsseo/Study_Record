# goal/urls.py
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.goal_list, name='goal_list')
]          #view파일에 있는 goal_list 함수 실행