# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import path, include

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    
    # users 앱의 인증 관련 URL
    path('auth/', include('users.urls')),
    
    # 메인 페이지 - 로그인 페이지로 리다이렉트
    path('', RedirectView.as_view(url='/auth/login.html'), name='index'),
]
    # 과목 관리 url
    path('subject/', include('subject.urls')),
]
