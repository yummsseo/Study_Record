from django.contrib import admin
from .models import Goal #model.py 파일 내부에 정의된 Goal 클래스를 가져와 사용함

# Register your models here.
admin.site.register(Goal)