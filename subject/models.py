from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_key = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    user_key = user_key = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.name 

class Subject(models.Model):
    subject_key = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    category_key = models.ForeignKey(Category, on_delete = models.CASCADE)
    user_key = models.ForeignKey(User, on_delete = models.CASCADE)
