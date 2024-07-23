# WeatherIntegration.py

import requests

def get_weather(city):
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]
        weather_report = {
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "pressure": main["pressure"],
            "weather_description": weather["description"],
            "wind_speed": wind["speed"]
        }
        return weather_report
    else:
        return "City Not Found"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
