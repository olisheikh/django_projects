from django.shortcuts import render
from django.http import HttpResponse 
from .models import Questions
from django.template import loader

# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)

def home(request):
    return HttpResponse('<h1>Home Screen</h1>')

def detail(request, question_id):
    return HttpResponse("You're looking for question %s." %question_id)

def results(request, question_id):
    response = "You're looking for result of a question %s"
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" %question_id)