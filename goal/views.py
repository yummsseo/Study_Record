from django.shortcuts import render
from django.db.models import Sum
from datetime import date, timedelta, datetime
from .models import Goal, Record

def goal_list(request):
    # 1. URL 파라미터에서 날짜 가져오기 (?date=2025-12-21 형태)
    date_str = request.GET.get('date')
    
    if date_str:
        try:
            # 주소창에 날짜가 있으면 그 날짜를 사용
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            # 날짜 형식이 잘못되었을 경우 오늘로 복귀
            target_date = date.today()
    else:
        # 주소창에 아무것도 없으면 오늘 날짜 사용
        target_date = date.today()

    # 2. 화살표 버튼을 위한 이전 날짜 / 다음 날짜 계산
    prev_date = (target_date - timedelta(days=1)).strftime('%Y-%m-%d')
    next_date = (target_date + timedelta(days=1)).strftime('%Y-%m-%d')
    
    # 3. 선택된 날짜(target_date)의 목표(Goal) 가져오기
    goal = Goal.objects.filter(goal_date=target_date).first()
    goal_time = goal.goal_time if goal else 0
    
    # 4. 선택된 날짜의 실제 기록(Record) 합계 계산
    total_recorded_time = Record.objects.filter(
        recorded_at__date=target_date # recorded_at 필드 날짜 기준
    ).aggregate(Sum('recorded_time'))['recorded_time__sum'] or 0
    
    # 5. 목표 달성률 계산
    achievement_percentage = 0
    if goal_time > 0:
        # 최대 100%까지만 표시하고 싶다면 min(...) 사용 가능
        achievement_percentage = round((total_recorded_time / goal_time) * 100, 1)

    # 6. HTML(템플릿)로 보낼 데이터 정리
    context = {
        'target_date': target_date,   # 현재 화면에 보이는 날짜
        'prev_date': prev_date,       # 화살표(이전) 링크용
        'next_date': next_date,       # 화살표(다음) 링크용
        'goal': goal,
        'goal_time': goal_time,
        'total_time': total_recorded_time,
        'percentage': achievement_percentage,
        'is_today': target_date == date.today(), # 오늘인지 확인용
    }
    
    return render(request, 'goal/goal_list.html', context)