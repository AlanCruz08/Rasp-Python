import json
import requests

def mandarDatos():
    # Ruta al archivo JSON en tu proyecto
    json_file_path = 'Datos.json'

    # Lee el contenido del archivo JSON
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    # Define la URL de la API a la que deseas realizar la solicitud POST
    api_url = "http://3.129.244.114/api/carga"
    # conexion api local
    #api_url = "http://127.0.0.1:8000/api/carga"

    try:
        print(json_data)
        # Realiza una solicitud POST a la API con el archivo JSON como body
        response = requests.post(api_url, json=json_data)
        #print(response.json())
        # Verifica si la solicitud fue exitosa (código de estado 2xx)
        if response.status_code // 100 == 2:
            # Imprime la respuesta en formato JSON
            print(response.json())
        else:
            # Imprime un mensaje de error si la solicitud no fue exitosa
            print(f"Error: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        # Captura y maneja excepciones relacionadas con la solicitud
        print(f"Error de solicitud: {e}")


if __name__ == '__main__':
    mandarDatos()