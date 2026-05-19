from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Task 1: Basic Student Model (Beginner)

# Create a model for a student.

# Requirements:
# name (string)
# age (integer)
# email (unique)
# enrolled_date (auto date)


class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_age = models.IntegerField(
        blank=False, null=False, validators=[MinValueValidator(6), MaxValueValidator(30)]
    )
    student_email = models.EmailField(unique=True)
    student_enrolled_date = models.DateField(auto_now_add=True)
    student_info_updated = models.DateField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 