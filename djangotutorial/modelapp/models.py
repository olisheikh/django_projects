from django.db import models
from enum import Enum

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    student_id = models.IntegerField(primary_key=True)
    
    class Meta:
        db_table = 'student'
        
class Teacher(models.Model):
    SHIRT_SIZE = {
        'S': 'Small',
        'M': 'Medium',
        'L': 'Large'
    }
    
    name = models.CharField(max_length=22)
    email = models.EmailField()
    date = models.DateField()
    ratings = models.CharField(max_length=2, choices=SHIRT_SIZE)
    
    
class Runner(models.Model):
    class MedalType(models.TextChoices):
        GOLD = "G", "Gold"
        SILVER = "S", "Silver"
        BRONZE = "B", "Braonze"
        
    MedalType = models.TextChoices("MedalType", "Gold Silver Bronze")
    name = models.CharField(max_length=20)
    medal = models.CharField(max_length=30, choices=MedalType)
    
    
    
    