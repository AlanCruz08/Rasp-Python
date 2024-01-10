import json
import requests


def mandarDatos(datos):
    #json_data = json.load(datos)

    api_url = "http://18.117.124.234/api/carga"
    # conexion api local
    #api_url = "http://127.0.0.1:8000/api/carga"

    try:
        response = requests.post(api_url, json=datos)
        # Verifica si la solicitud fue exitosa (código de estado 2xx)
        if response.status_code // 100 == 2:
            print("Datos enviados al servidor")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")

