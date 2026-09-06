from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Boston"):
    api_key = os.getenv("API_KEY")
    request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'

    response = requests.get(request_url)
    if response.status_code != 200:
        return None

    return response.json()

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")
    if not bool(city.strip()):
        city = "Boston"
        
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
