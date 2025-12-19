from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Category, Subject, Record, Goal
from .forms import CategoryForm, SubjectForm
import math

@login_required(login_url='login_html')
def dashboard(request):
    user = request.user

    if request.method == "POST":
        action = request.POST.get('action')

        if action == 'add_category':
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.user_key = user
                category.save()
                return redirect('dashboard')

        elif action == 'add_subject':
            form = SubjectForm(request.POST, user=user) 
            if form.is_valid():
                subject = form.save(commit=False)
                subject.user_key = user
                subject.save()
                return redirect('dashboard')

        elif action == 'delete_subject':
            selected_subjects = request.POST.getlist('selected_subjects')
            if selected_subjects:
                Subject.objects.filter(subject_key__in=selected_subjects, user_key=user).delete()
            return redirect('dashboard')
        
        elif action == 'delete_category':
            selected_categories = request.POST.getlist('selected_categories')
            if selected_categories:
                Category.objects.filter(category_key__in=selected_categories, user_key=user).delete()
            return redirect('dashboard')

    category_form = CategoryForm()
    subject_form = SubjectForm(user=user)

    Category.objects.get_or_create(name="기본", user_key=user)
    categories = Category.objects.filter(user_key=user)

    data = []
    for category in categories:
        subjects = Subject.objects.filter(category_key=category, user_key=user)
        data.append({
            'category': category,
            'subjects': subjects
        })

    context = {
        'category_form': category_form,
        'subject_form': subject_form,
        'data': data,
        'categories': categories
    }
    
    return render(request, "subject/dashboard.html", context)


@login_required(login_url='login_html')
def time_measure(request):
    user = request.user
    today = timezone.now().date()
    
    subjects = Subject.objects.filter(user_key=user)

    if request.method == "GET":
        return render(request, "subject/time_measure_view.html", {"subjects" : subjects})

    elif request.method == "POST":
        subject_id = request.POST.get('subject_key')
        time_seconds = request.POST.get('time_seconds')

        if subject_id and time_seconds:
            subject = get_object_or_404(Subject, pk=subject_id)

            goal, created = Goal.objects.get_or_create(
                user=user, 
                goal_date=today, 
                defaults={'goal_time':60}
            )
            
            seconds = int(time_seconds)
            minutes = math.ceil(seconds / 60)
            
            Record.objects.create(
                user=user, goal=goal, 
                subject=subject, 
                recorded_time=minutes, 
                recorded_at=timezone.now()
            )
            
            return redirect('dashboard') 
        
        else:
            return render(request, "subject/time_measure_view.html", {"subjects": subjects})