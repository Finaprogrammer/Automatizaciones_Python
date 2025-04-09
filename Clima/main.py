import requests
from datetime import datetime


def get_weather(city):
    """obtienes el clima actual de una ciudad usando la api de openweathermap"""

    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    try:
        #hacer la peticion a la api
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # celsius  
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        #procesar datos del clima
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # imprimir informacion del clima
        print(f"/nclima en {weather['city']}:\n")
        print(f"Temperatura: {weather['temperature']}°C")
        print(f"Descripcion: {weather['description']}")
        print(f"Humedad: {weather['humidity']}%")
        print(f"Hora: {weather['time']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

if name__ == "__main__":
    city = input("Introduce el nombre de la ciudad: ")
    get_weather(city)
    # get_weather(city) 
        


