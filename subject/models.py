from django.db import models
from django.utils import timezone

# 앱 합치면 삭제해야함 (user_key 참조용 임시 테이블)
class Temp(models.Model):
    user_key = models.IntegerField(primary_key = True)

class Category(models.Model):
    category_key = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    user_key = user_key = models.ForeignKey(Temp, on_delete = models.CASCADE)
    def __str__(self):
        return self.name 

class Subject(models.Model):
    subject_key = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    category_key = models.ForeignKey(Category, on_delete = models.CASCADE)
    user_key = models.ForeignKey(Temp, on_delete = models.CASCADE)

class Record(models.Model):
    record_key = models.AutoField(primary_key = True)
    user_key = models.ForeignKey(Temp, on_delete = models.CASCADE) #앱 합칠때 참조할 테이블 변경해야함 (Temp -> 앱이름.모델명)
    subject_key=models.ForeignKey(Subject, on_delete = models.SET_NULL, null = True)
    date = models.DateField(default=timezone.now)
    time = models.DurationField()
