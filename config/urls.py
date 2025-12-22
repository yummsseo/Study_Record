from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),

    # 1. goal 앱 연결 (http://127.0.0.1:8000/goal/)
    path('goal/', include('goal.urls')),

    # 2. dash 앱 연결 (http://127.0.0.1:8000/dash/)
    path('dash/', include('dash.urls')),

    path('auth/', include('users.urls')),
    
    # 메인 페이지 - 로그인 페이지로 리다이렉트
    path('', RedirectView.as_view(url='/auth/login.html'), name='index'),
    
    # 과목 관리 url
    path('subject/', include('subject.urls')),
]
