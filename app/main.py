import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "https://api.weatherapi.com/v1/current.json"
city = "Paris"
country = "France"
url = f"{base_url}?key={api_key}&q={city}"


def get_weather() -> None:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            condition = weather_data["current"]["condition"]["text"]
            temp_c = weather_data["current"]["temp_c"]
            time = weather_data["location"]["localtime"]
            print(f"{city}/{country} {time} Weather: {temp_c} Celsius, {condition}")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
