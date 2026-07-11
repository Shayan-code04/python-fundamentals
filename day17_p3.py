import os
import json
import requests


def fetch_weather(city):
    """
    Fetch weather data from OpenWeatherMap API.
    """

    api_key = os.environ.get("OWM_API_KEY")

    if not api_key:
        print("Error: OWM_API_KEY environment variable not found.")
        print("Set your API key before running the program.")
        return None

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={api_key}"
        f"&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 401:
        print("Error: Invalid API Key.")
        return None

    elif response.status_code == 404:
        print("Error: City not found.")
        return None

    else:
        print(f"Unexpected Error: {response.status_code}")
        return None


def display_weather(data):
    """
    Display weather information in a readable format.
    """

    print("\n========== Weather Report ==========\n")

    print(f"City        : {data['name']}")
    print(f"Country     : {data['sys']['country']}")
    print(f"Temperature : {data['main']['temp']} °C")
    print(f"Feels Like  : {data['main']['feels_like']} °C")
    print(f"Humidity    : {data['main']['humidity']} %")
    print(f"Pressure    : {data['main']['pressure']} hPa")
    print(f"Weather     : {data['weather'][0]['main']}")
    print(f"Description : {data['weather'][0]['description']}")
    print(f"Wind Speed  : {data['wind']['speed']} m/s")


def save_to_file(data, filename):
    """
    Save weather data to a JSON file.
    """

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():

    city = input("Enter city name: ")

    data = fetch_weather(city)

    if data:
        display_weather(data)
        save_to_file(data, "weather.json")
        print("\nWeather data saved to weather.json")


if __name__ == "__main__":
    main()