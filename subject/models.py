from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category_key = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    user_key = user_key = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.name 

class Subject(models.Model):
    subject_key = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    category_key = models.ForeignKey(Category, on_delete = models.CASCADE)
    user_key = models.ForeignKey(User, on_delete = models.CASCADE)

# 기존에 작성했던 record 테이블
# class Record(models.Model):
#     record_key = models.AutoField(primary_key = True)
#     user_key = models.ForeignKey(User, on_delete = models.CASCADE) #앱 합칠때 참조할 테이블 변경해야함 (Temp -> 앱이름.모델명)
#     subject_key=models.ForeignKey(Subject, on_delete = models.SET_NULL, null = True)
#     date = models.DateField(default=timezone.now)
#     time = models.DurationField()


# 테스트용 임시 코드
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_time = models.PositiveIntegerField(default=60)
    goal_date = models.DateField(default=timezone.now)

    class Meta:
        pass

class Record(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    recorded_time = models.PositiveIntegerField(default=0)
    recorded_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)