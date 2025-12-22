from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.dashBoard, name='dashBoard')
]          #view파일에 있는 dashBoard 함수 실행