import requests
import re
api_key_check = re.compile(r'^[a-f0-9]{32}$')
temperature_check = re.compile(r'^\d+(\.\d+)?$')
weather_condition_check = re.compile(r'^[a-zA-Z0-9\s]+$')


def get_weather(city):
    try:
        api_key = 'd5f78285b26695165adf5d0bbcae82cc'
        if not api_key_check.match(api_key):
            print('Invalid API key format.')
            return
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(api_url)
        response.raise_for_status()  # Raise  exception 

        weather_data = response.json()
        temperature = weather_data['main']['temp']
        if not temperature_check.match(str(temperature)):
            print('Invalid temperature value received from the API.')
            return

        weather_condition = weather_data['weather'][0]['description']
        if not weather_condition_check.match(weather_condition):
            print('Invalid weather condition value received from the API.')
            return

        print(f'Weather in {city}:')
        print(f'Temperature: {temperature}°C')
        print(f'Weather Condition: {weather_condition}')
    except Exception as error:
        print(f'Failed to retrieve weather data. Error: {error}')


# Define the city directly in the code
city_to_scrape = 'Karachi'

# Call the function to get weather data
get_weather(city_to_scrape)
