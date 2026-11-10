import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 2.4419,
    "longitude": -76.6063,
    "current": "temperature_2m,wind_speed_10m"
}

respuesta = requests.get(url, params=params)

datos = respuesta.json()

print("Clima actual de Popayan")
print("Temperatura:", datos["current"]["temperature_2m"], "°C")
print("Velocidad del viento:", datos["current"]["wind_speed_10m"], "km/h")