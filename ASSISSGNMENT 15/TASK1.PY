import requests
import json


def display_weather(city_name):
    api_key = "ac2e0bfc705f8483aefafbfce3d86f0e"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    print(json.dumps(weather_data, indent=4))

# Example usage
city = input("Enter city name: ")
display_weather(city)
