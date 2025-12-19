from django import forms
from .models import Category, Subject

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SubjectForm(forms.ModelForm):
    category_key = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        empty_label="카테고리 선택",
        label="카테고리"
    )

    class Meta:
        model = Subject
        fields = ['name', 'category_key']
        labels = {'name': '과목명'}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category_key'].queryset = Category.objects.filter(user_key=user)
