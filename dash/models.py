from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

#수동으로 기록 추가/수정/삭제
#필요한 속성은?
# dash/models.py


# Django의 기본 User 모델을 가져옵니다.
User = get_user_model()

# =========================================================
# 1. Subject 모델: 학습 과목 관리
# =========================================================
class Subject(models.Model):
    """
    사용자가 등록한 학습 과목의 정보를 저장합니다.
    """
    # 💡 1:N 관계: 하나의 User는 여러 개의 Subject(과목)를 등록할 수 있습니다.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 과목 이름 (필수, 고유하게 설정하여 중복 방지)
    name = models.CharField(max_length=100)
    
    # (선택 사항) 과목의 색상 코드 (시각화 시 활용)
    color_code = models.CharField(max_length=7, default="#007BFF") # 예: HTML 색상 코드

    def __str__(self):
        return f"{self.user.username}의 과목: {self.name}"

    class Meta:
        # 특정 유저가 같은 이름의 과목을 등록하지 못하도록 제약 조건 추가
        unique_together = ('user', 'name')
        verbose_name_plural = "Subjects (과목)"
