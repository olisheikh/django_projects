from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    person = Person.objects.all()
    
    return render(request, 'modelapp/model.html', {
        'person': person
    })

