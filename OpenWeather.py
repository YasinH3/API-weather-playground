import requests


API_KEY = "2c59f5835e38c0cce167099d5b69e026"
city = "Madrid"

url = "https://api.openweathermap.org/data/2.5/weather"


params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

print(response.json())