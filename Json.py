import json
import requests
from datetime import datetime
from servidor import mandarDatos

class ClssJson:

    def guardar(datos_nuevos, nombre_archivo="Datos.json"):
        datos_existen = []
        
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos_existen = json.load(archivo)
        except Exception as e:
            print(f"Error al leer el archivo {nombre_archivo}: {e}")

        for dato_nuevo in datos_nuevos:
            # Verificar si hay un elemento existente con la misma fecha, tipo y sensor
            duplicado = any(
                datetime.strptime(dato_existente['fecha'], '%Y-%m-%d %H:%M:%S') == datetime.strptime(dato_nuevo['fecha'], '%Y-%m-%d %H:%M:%S')
                and dato_existente['tipo'] == dato_nuevo['tipo']
                and dato_existente['nSensor'] == dato_nuevo['nSensor']
                and dato_existente['valor'] == dato_nuevo['valor']
                for dato_existente in datos_existen
            )

            # Si no es un duplicado, agregarlo
            if duplicado is False:
                datos_existen.append(dato_nuevo)

        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_existen, archivo, indent=4)
        conectado = ClssJson.is_connected_to_internet()

        if conectado:
            mandarDatos(datos_existen)
            with open(nombre_archivo, 'w') as archivo:
                json.dump([], archivo)

    def is_connected_to_internet():
        try:
            requests.get('http://google.com')
            return True
        except requests.exceptions.RequestException as e:
            return False

    def importar(nombreArchivo):
        with open(nombreArchivo, 'r') as archivo:
            diccionario = json.load(archivo)
        return diccionario