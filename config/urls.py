from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # 1. goal 앱 연결 (http://127.0.0.1:8000/goal/)
    path('goal/', include('goal.urls')),

    # 2. dash 앱 연결 (http://127.0.0.1:8000/dash/)
    path('dash/', include('dash.urls')),
    
    # (선택사항) 만약 주소창에 아무것도 안 쳤을 때(http://127.0.0.1:8000/) 
    # 바로 대시보드로 가게 하고 싶다면 아래 줄을 추가하세요.
    # path('', include('dash.urls')), 
]