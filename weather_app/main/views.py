from django.shortcuts import render
import requests
from .models import SearchHistory

# Create your views here.
API_KEY = '3e8479e453ce01367e6f54479336dcd9'

def index(request):
    weather = None 
    error = None 
    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
    
    if request.method == "POST":
        city = request.POST.get('city', '').strip()
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                resp = requests.get(url, timeout=5)
                data = resp.json()
                if resp.status_code == 200:
                    weather = {'city': f"{data['name']}, {data['sys'] ['country']}",
                               'temperature': data['main'] ['temp'],
                               'humidity': data['main'] ['humidity'],
                               'pressure': data['main'] ['pressure'],
                               'description': data['weather'][0]['description'].title(),
                               'icon': data['weather'][0]['icon']}
                    
                    SearchHistory.objects.create(
                        city_name = data['name'],
                        temparature = data['main']['temp'],
                        humidity = data['main']['humidity'],
                        pressure = data['main']['pressure'],
                        description = data['weather'][0]['description'].title()
                    )
                    
                    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
                else:
                    error = data.get('message', 'could not fetch weather data.')
            except requests.RequestException: 
                error = 'Notwork error. Please try again.'
        else:
                    error = "Please enter a city name!!!"
    return render(request, "main/index.html", {
                'weather': weather,
                'error': error,
                'recent_searches': recent_searches
            })
