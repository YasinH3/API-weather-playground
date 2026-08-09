import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if len(sys.argv) > 1:
    city = " ".join(sys.argv[1:])
else:
    city = input("Enter the city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]
    print(f"Weather in {city}: {weather['description'].capitalize()}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
    print(f"Coordinates: Latitude {data['coord']['lat']}, Longitude {data['coord']['lon']}")

else:
    print(f"Error: {response.status_code} - {response.text}")