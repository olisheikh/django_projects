from django.shortcuts import render, redirect
from django.http import HttpResponse 
# Create your views here.

students = [
    {
        'id':1,
        'name':'Alex',
        'email': 'alex@gmail.com',
        'department': 'CSE',
        'slug': 'alex-name'
    },
    {
        'id':2,
        'name':'bob',
        'email': 'bob@gmail.com',
        'department': 'EEE',
        'slug': 'bob-name'
    },
    {
        'id':3,
        'name':'Cherry',
        'email': 'cherry@gmail.com',
        'department': 'IPE',
        'slug': 'cherry-name'
    },
]

def student_list(request):
    return render(request, students/student_list.html, {
        'students': students 
    })
    
def student_details(request, id):
    student = None 
    
    for item in students:
        if item['id'] == id:
            student = item
            break
        
    if student == None:
        return HttpResponse('Student not found', status=404)

    return render(request, 'students/student_detail.html', {
        'student': student
    })
    
def student_profile(request, slug):
    student = None 
    for item in students:
        if item['slug'] == slug:
            student = item
            break
        
    if student in None:
        return 