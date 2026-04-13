from django.contrib import admin
from .models import Person, Teacher, Student, Runner
# Register your models here.

admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Runner)
