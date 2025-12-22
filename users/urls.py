# users/urls.py

from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # HTML 템플릿 뷰
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login_html'),
    path('signup.html', TemplateView.as_view(template_name='signup.html'), name='signup_html'),
    path('logout.html', TemplateView.as_view(template_name='logout.html'), name='logout_html'),
    
    # API 엔드포인트
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]