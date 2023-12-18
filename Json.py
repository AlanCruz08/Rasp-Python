import json
import requests
from servidor import mandarDatos


class ClssJson:

    def guardar(datos_nuevos, nombre_archivo="Datos.json"):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos_existen = json.load(archivo)
        except FileNotFoundError:
            datos_existen = []

        if not datos_existen and ClssJson.is_connected_to_internet():
            mandarDatos(datos_existen)
            datos_existen = []

        datos_existen.extend(datos_nuevos)

        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_existen, archivo, indent=4)

    def is_connected_to_internet(self):
        try:
            requests.get('http://google.com')
            return True
        except requests.exceptions.RequestException as e:
            return False

    def importar(nombreArchivo):
        with open(nombreArchivo, 'r') as archivo:
            diccionario = json.load(archivo)
        return diccionario


if __name__ == '__main__':
    clss = ClssJson()
    clss.guardar()