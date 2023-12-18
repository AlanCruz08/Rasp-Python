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
            fecha_nueva = datetime.strptime(dato_nuevo['fecha'], '%Y-%m-%d %H:%M:%S')
            tipo_nuevo = dato_nuevo['tipo']
            nSensor_nuevo = dato_nuevo['nSensor']

            # Verificar si hay un elemento existente con la misma fecha, tipo y sensor
            duplicado = any(
                datetime.strptime(dato_existente['fecha'], '%Y-%m-%d %H:%M:%S') == fecha_nueva
                and dato_existente['tipo'] == tipo_nuevo
                and dato_existente['nSensor'] == nSensor_nuevo
                for dato_existente in datos_existen
            )

            # Si no es un duplicado, agregarlo
            if not duplicado:
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


if __name__ == '__main__':
    clss = ClssJson()
    clss.guardar()