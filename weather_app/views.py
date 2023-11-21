from django.shortcuts import render
from datetime import datetime
import requests 
from django.http import HttpResponse, JsonResponse



def weather_info(request):
    if request.method == 'POST':
        city_name = request.POST['city_name']
        api_key = ''  # Replace with your API key

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city_name.lower()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data["cod"] != "404":
            main_info = weather_data["main"]
            temperature = main_info["temp"]
            pressure = main_info["pressure"]
            humidity = main_info["humidity"]
            weather_description = weather_data["weather"][0]["description"]
        else:
            return render(request, 'index.html', {'error_message': 'City not found'})

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        context = {
            'temperature': temperature,
            'pressure': pressure,
            'humidity': humidity,
            'description': weather_description,
            'current_time': current_time,
        }
    else:
        context = {}  # Initial rendering

    return render(request, 'index.html', context)