from django.shortcuts import render, redirect
from datetime import timedelta
from .models import *
from .forms import *

temp, created=Temp.objects.get_or_create(user_key=1) #

def subject_main(request):
    if not Category.objects.filter(user_key=temp).exists():
        Category.objects.create(name="기본",user_key=temp)
    categories = Category.objects.filter(user_key=temp)


    data = []
    for i in categories:
        subjects = Subject.objects.filter(category_key=i)
        if subjects.exists():
            data.append({
                'category': i,
                'subjects': subjects
            })
        else:
            data.append({
                'category': i,
                'subjects': None
            })
    return render(request,"subject_main_view.html", {'data': data})


def subject_delete(request):
    if request.method=="POST":
        selected_subject = request.POST.getlist('select')
        Subject.objects.filter(subject_key__in=selected_subject).delete()
    return redirect('subject_main_view')


def subject_add(request):
    if request.method=="GET":
        form=SubjectForm()
        form.fields['category_key'].queryset = Category.objects.filter(user_key=1)
        return render(request,"subject_add_view.html", {"form":form})
    
    if request.method=="POST":
        form=SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user_key = temp
            subject.save()
            return redirect('subject_add_view')
        else:
            return render(request, "subject_add_view.html", {"form": form})
    

def category_manage(request):
    if request.method=="GET":
        form=CategoryForm()
        categories=Category.objects.filter(user_key=temp)
        return render(request,"category_manage_view.html", {"form": form, "categories" : categories})
    elif request.method=="POST":
        if request.POST.get("action")=='delete':
            selected_category=request.POST.getlist('select')
            Category.objects.filter(category_key__in=selected_category).delete()
            return redirect('category_manage_view')
        elif request.POST.get("action")=='update':
            form=CategoryForm(request.POST)
            if form.is_valid():
                category = form.save(commit=False)
                category.user_key = temp
                category.save()
                return redirect('category_manage_view')
            else:
                categories=Category.objects.filter(user_key=temp)
            return render(request,"category_manage_view.html", {"form": form, "categories" : categories})

def time_measure(request):
        return render(request, "time_measure_view.html")
