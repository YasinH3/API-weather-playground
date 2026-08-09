import requests
import sys

if len(sys.argv) > 1:
    city = " ".join(sys.argv[1:])
else:
    city = input("Enter the city name: ")

geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                   params={"name": city, "count": 1}
).json()

location = geo["results"][0]

weather = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": location["latitude"],
                "longitude": location["longitude"],
                "current":"temperature_2m"}
).json()

print(f"{location['name']}: {weather['current']['temperature_2m']}°C")
                                    