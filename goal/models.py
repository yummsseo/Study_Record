from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model 
from django.utils import timezone

# Django의 기본 User 모델을 안전하게 가져옵니다.
User = get_user_model() 

# =========================================================
# 1. Goal 모델: 일별 학습 목표 설정
# =========================================================
class Goal(models.Model):
    """
    사용자가 설정한 특정 날짜의 목표 학습 시간 (분 단위)을 저장합니다.
    """
    
    # 💡 1:N 관계: 하나의 User는 여러 개의 Goal(목표)을 가집니다.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 목표 학습 시간 (분 단위)
    # 최소 1분 이상의 시간을 입력하도록 PositiveIntegerField 사용
    goal_time = models.PositiveIntegerField(default=60) 
    
    # 목표 설정 날짜 (날짜는 유일해야 합니다. 한 날짜에 목표가 두 개일 필요는 없음)
    goal_date = models.DateField(default=timezone.now) 

    def __str__(self):
        return f"{self.user.username}의 {self.goal_date} 목표 ({self.goal_time}분)"

    class Meta:
        # Django 관리자 페이지에서 볼 때 복수형 이름 설정
        verbose_name_plural = "Goals (일별 목표)"
        # 특정 유저가 같은 날짜에 두 개의 목표를 설정하지 못하도록 제약 조건 추가 (추가적인 안전 장치)
        unique_together = ('user', 'goal_date')


# =========================================================
# 2. Record 모델: 실제 학습 시간 기록
# =========================================================

class Record(models.Model):
    
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    recorded_time = models.PositiveIntegerField(default=0) 
    recorded_at = models.DateTimeField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 💡 핵심 수정: 'dash.Subject'를 문자열로 참조
    # Django는 이 문자열을 보고 'dash' 앱에서 'Subject' 모델을 찾습니다.
    subject = models.ForeignKey(
        'dash.Subject', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    ) 

    def __str__(self):
        # 문자열로 참조했기 때문에 __str__ 내부에서도 직접 Subject를 참조할 수 없습니다.
        # 아래처럼 .name을 사용하려면 __str__ 메서드 상단에 import를 살려두거나, 
        # 혹은 이 메서드를 잠시 주석 처리하고 마이그레이션을 진행합니다.
        # 당장은 마이그레이션이 목적이므로 __str__ 메서드는 잠시 단순화하거나 주석 처리해도 좋습니다.
        return f"{self.recorded_time}분 기록"
    
    class Meta:
        verbose_name_plural = "Records (학습 기록)"
'''
class Record(models.Model):
    """
    사용자가 특정 목표를 위해 실제로 학습한 시간을 기록합니다.
    """
    
    # 💡 1:N 관계: 하나의 Goal(목표)은 여러 개의 Record(학습 기록)를 가질 수 있습니다.
    # 예: 오전 30분, 오후 45분
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    
    # 실제 학습한 시간 (분 단위)
    # 이 시간을 모두 합산하여 목표 달성률을 계산합니다.
    recorded_time = models.PositiveIntegerField(default=0) 
    
    # 기록이 생성된 시간 (언제 학습했는지)
    recorded_at = models.DateTimeField()

# 💡 새로운 외래 키: 어떤 과목에 대한 기록인가?
    # 1:N 관계: 하나의 Subject는 여러 개의 Record를 가질 수 있습니다.
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.goal.goal_date} - {self.recorded_time}분 기록"
    
    class Meta:
        verbose_name_plural = "Records (학습 기록)"

# 목표 설정/관리에서 구현해야 할 속성은?
# 학습시간, 
class Goal(models.Model):
    #일간 목표 설정
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    goal_time = models.IntegerField(default=0) #사용자에게 시간을 입력받아 저장(분단위?)
    goal_date = models.DateField() #언제의 목표인가?

    #목표 달성률 표시
    
    
#학습시간 기록
#class Record(models.Model):

#장고의 외래키는 1:N의 관계를 나타낼 수 있다.(질문은 하나, 답변은 여러 개 등)
#하나의 목표는 여러 개의 기록을 가진다.
#목표 설정 일간으로 분배
'''