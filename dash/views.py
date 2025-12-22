from django.shortcuts import render
from django.db.models import Sum
from datetime import date
# 우리가 만들었던 goal 앱의 모델들을 가져옵니다.
from goal.models import Goal, Record 

def dashBoard(request):
    # 1. 오늘 날짜를 구함
    today = date.today()
    
    # 2. 오늘 날짜에 해당하는 목표(Goal) 정보를 DB에서 가져옴
    goal = Goal.objects.filter(goal_date=today).first()
    goal_time = goal.goal_time if goal else 0
    
    # 3. 오늘 날짜에 해당하는 실제 기록(Record)들의 시간을 합산함
    total_time = Record.objects.filter(recorded_at__date=today).aggregate(Sum('recorded_time'))['recorded_time__sum'] or 0
    
    # 4. 빈 접시 대신 '데이터가 담긴 접시'를 만듭니다. (Context)
    context = {
        'today': today,
        'goal_time': goal_time,
        'total_time': total_time,
        # 달성률 계산 (0으로 나누기 방지)
        'achievement_rate': round((total_time / goal_time * 100), 1) if goal_time > 0 else 0,
    }
    
    # 5. 이제 데이터가 담긴 context를 HTML로 넘겨줍니다.
    return render(request, 'dash/dashboard.html', context)