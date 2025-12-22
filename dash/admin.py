from django.contrib import admin
# 💡 Subject 모델을 import 합니다.
from subject.models import Subject 

# Subject 모델을 관리자 페이지에 등록할 때,
# 괄호 안에 등록할 모델을 명시해야 합니다.
admin.site.register(Subject)