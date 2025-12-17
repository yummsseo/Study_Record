"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Study_Record/urls.py
from django.contrib import admin
from django.urls import path, include #inlcude도 import해주어야 한다.

# 리스트 안에 있는 path의 url 패턴(첫번째 인자)들에 따라서,
# 패턴이 일치하면 실행할 함수(두번째인자)를 매칭 시켜준다.
urlpatterns = [
<<<<<<< HEAD
    path("admin/", admin.site.urls),

     #'앱명/', include('앱명.urls')형식
    path('goal/', include('goal.urls')),
=======
    path("/", admin.site.urls),
>>>>>>> 8c5b8ee8e38dfc265233bbc40f898f90fdc2f2e4
]
