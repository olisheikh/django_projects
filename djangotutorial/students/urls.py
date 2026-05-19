from django.urls import path 
from . import views

app_name = "students"

urlpatterns = [
    # Student 
    path('', views.student_list, name = "list")
    
    # student/create
    path('create/', views.student_create, name = 'create')
    
    path('<int:id>/', views.student_detail, name='detail')
    
    path('profile/<slug:slug>', views.student_profile, name='profile')
    path('contact/', views.contact, name='contact')
    path('go-home/', views.go_home, name='go_home')
    
]