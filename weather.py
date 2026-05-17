import requests

from config import WEATHER_API_KEY

def get_weather(city="Omsk"):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=metric"
        f"&lang=ru"
    )

    response = requests.get(url)

    data = response.json()

    weather = data["weather"][0]["main"]

    return weather