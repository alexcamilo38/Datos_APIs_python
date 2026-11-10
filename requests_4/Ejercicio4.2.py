import requests

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
        print("Error al conectar con el servicio del clima.")
        return None


clima = consultar_clima(2.4419, -76.6063)

if clima is not None:
    print("Temperatura:", clima["current"]["temperature_2m"], "°C")
    print("Velocidad del viento:", clima["current"]["wind_speed_10m"], "km/h")