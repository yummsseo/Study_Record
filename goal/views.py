from django.shortcuts import render, redirect  # 1. redirect가 꼭 있어야 합니다!
from django.db.models import Sum
from datetime import date, timedelta, datetime
from .models import Goal, Record

def goal_list(request):
    # --- [1. 저장 로직: POST 요청 처리] ---
    if request.method == "POST":
        target_date_str = request.POST.get('goal_date')
        new_time = request.POST.get('goal_time')
        
        if target_date_str and new_time:
            # 해당 날짜에 데이터가 있으면 수정, 없으면 생성
            Goal.objects.update_or_create(
                goal_date=target_date_str,
                user=request.user,
                defaults={'goal_time': new_time}
            )
        # 저장이 끝나면 반드시 redirect를 해줘야 500 에러가 안 납니다!
        return redirect(f"/goal/?date={target_date_str}")

    # --- [2. 조회 로직: 화면 보여주기] ---
    date_str = request.GET.get('date')
    
    if date_str:
        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            target_date = date.today()
    else:
        target_date = date.today()

    # 날짜 계산
    prev_date = (target_date - timedelta(days=1)).strftime('%Y-%m-%d')
    next_date = (target_date + timedelta(days=1)).strftime('%Y-%m-%d')
    
    # 데이터 가져오기
    goal = Goal.objects.filter(goal_date=target_date).first()
    goal_time = goal.goal_time if goal else 0
    
    total_recorded_time = Record.objects.filter(
        recorded_at__date=target_date
    ).aggregate(Sum('recorded_time'))['recorded_time__sum'] or 0
    
    achievement_percentage = 0
    if goal_time > 0:
        achievement_percentage = round((total_recorded_time / goal_time) * 100, 1)

    context = {
        'target_date': target_date,
        'prev_date': prev_date,
        'next_date': next_date,
        'goal': goal,
        'goal_time': goal_time,
        'total_time': total_recorded_time,
        'percentage': achievement_percentage,
        'is_today': target_date == date.today(),
    }
    
    return render(request, 'goal/goal_list.html', context)