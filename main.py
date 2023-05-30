import requests
import json
import sys

API_KEY = "e18c92b85061696b7eb38cc66e046fd4"  # Replace with your OpenWeatherMap API key

def get_weather_forecast(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        # requests weather status as json object
        response = requests.get(url) 
        # check the status
        response.raise_for_status()

        # convert the json object to dictionary
        data = json.loads(response.text)

        # get the weather and its description along with temperature and humidity
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # print weather status
        print(f"Weather forecast for {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        # exception in https request or key error or any other error that may occur
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Invalid response format for {city}. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <city>")
    else:
        city = sys.argv[1]
        get_weather_forecast(city)
