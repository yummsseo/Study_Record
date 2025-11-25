from django.shortcuts import render

# Create your views here.

def goal_list(request):
    return render(request, 'goal/goal_list.html', {})
                #첫번째 인자/두번째 인자(앱명/html주소)/세번째 인자(모델의 값)