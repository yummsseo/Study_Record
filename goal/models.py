from django.db import models

# Create your models here.

# 목표 설정/관리에서 구현해야 할 속성은?
# 학습시간, 
class Goal(models.Model):
    goal_time = models.IntegerField() #사용자에게 시간을 입력받아 저장
    created_at = models.DateTimeField(auto_now_add=True) #해당 레코드 생성시 해당 날짜 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 해당 날짜 자동저장