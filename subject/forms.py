from django import forms
from .models import Category, Subject

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubjectForm(forms.ModelForm):
    category_key = forms.ModelChoiceField(
        queryset=Category.objects.filter(user_key=1),
        empty_label="카테고리 선택",
        label="카테고리"
    )

    class Meta:
        model = Subject
        fields = ['name', 'category_key']
        labels = {'name': '과목명'}
