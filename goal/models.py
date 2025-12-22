from django.db import models
from django.contrib.auth import get_user_model 
from django.utils import timezone
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_time = models.PositiveIntegerField(default=60) 
    goal_date = models.DateField(default=timezone.now) 

    def __str__(self):
        return f"{self.user.username}의 {self.goal_date} 목표 ({self.goal_time}분)"

    class Meta:
        verbose_name_plural = "Goals (일별 목표)"
        unique_together = ('user', 'goal_date')

class Record(models.Model):
    
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    recorded_time = models.PositiveIntegerField(default=0) 
    recorded_at = models.DateTimeField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    subject = models.ForeignKey(
        'subject.Subject', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    ) 

    def __str__(self):
        return f"{self.recorded_time}분 기록"
    
    class Meta:
        verbose_name_plural = "Records (학습 기록)"
