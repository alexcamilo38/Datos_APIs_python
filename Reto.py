import requests
import json

# Ciudades con sus coordenadas
ciudades = {
    "Popayán": (2.4419, -76.6063),
    "Bogotá": (4.7110, -74.0721),
    "Cali": (3.4516, -76.5320),
    "Medellín": (6.2442, -75.5812)
}


# Función para consultar el clima
def consultar_clima(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }

    try:
        respuesta = requests.get(url, params=params, timeout=10)

        respuesta.raise_for_status()

        datos = respuesta.json()

        return datos["current"]["temperature_2m"]

    except (requests.exceptions.RequestException, KeyError, TypeError):
        print("No se pudo consultar el clima de una ciudad.")
        return None

temperaturas = {}

for ciudad, coordenadas in ciudades.items():

    lat, lon = coordenadas

    temperatura = consultar_clima(lat, lon)

    if temperatura is not None:

        temperaturas[ciudad] = temperatura

        print(ciudad, ":", temperatura, "°C")



with open("clima_ciudades.json", "w", encoding="utf-8") as f:

    json.dump(temperaturas, f, indent=4, ensure_ascii=False)


 
with open("clima_ciudades.json", "r", encoding="utf-8") as f:

    datos = json.load(f)



if datos:

    ciudad_mas_caliente = max(datos, key=datos.get)

    print("\nLa ciudad más calurosa es:", ciudad_mas_caliente)

    print("Temperatura:", datos[ciudad_mas_caliente], "°C")

else:

    print("No se pudieron consultar las temperaturas.")