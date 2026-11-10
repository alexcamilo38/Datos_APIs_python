import requests
import json

def consultar_clima(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }

    try:
        respuesta = requests.get(url, params=params, timeout=10)

        respuesta.raise_for_status()

        datos = respuesta.json()

        return datos

    except requests.exceptions.RequestException:
        print("Error al consultar el clima.")
        return None


# Consultar el clima de Popayán
clima = consultar_clima(2.4419, -76.6063)

if clima is not None:

 
    with open("clima.json", "w", encoding="utf-8") as archivo:
        json.dump(clima, archivo, indent=4, ensure_ascii=False)


    with open("clima.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    print("Temperatura de Popayán:")
    print(datos["current"]["temperature_2m"], "°C")