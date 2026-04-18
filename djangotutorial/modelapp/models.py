from django.db import models
from enum import Enum

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.first_name + self.last_name
    
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
    
    
class Fruit(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    
# Relationship

# many-to-many

    
class Group(models.Model):
    name = models.CharField(max_length=128)    
    members = models.ManyToManyField(Person, through="Membership")
    
    def __str__(self):
        return self.name 
    
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()

    class Meta:
        # ✅ Valid Meta options
        db_table = 'new_membership'
        ordering = ['date_joined']
        unique_together = [['person', 'group']]  # ← if you wanted uniqueness constraint

# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)
    
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['person', 'group'],
#                 name = "unique_person_group"
#             )
#         ]