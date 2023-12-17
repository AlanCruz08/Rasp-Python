import json
import requests


def mandarDatos():
    json_file_path = 'Datos.json'

    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    api_url = "http://3.129.244.114/api/carga"
    # conexion api local
    # api_url = "http://127.0.0.1:8000/api/carga"

    try:
        response = requests.post(api_url, json=json_data)
        # Verifica si la solicitud fue exitosa (código de estado 2xx)
        if response.status_code // 100 == 2:
            print("Datos enviados al servidor")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")


if __name__ == '__main__':
    mandarDatos()
