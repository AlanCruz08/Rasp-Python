import json


class ClssJson:
    
    def guardar(datos_nuevos, nombre_archivo="archivo.json"):
        datos_existen = []

        try:
            with open(nombre_archivo, 'r') as archivo:
                datos_existen = json.load(archivo)
        except FileNotFoundError:
            pass

        for dato_nuevo in datos_nuevos:
            if dato_nuevo not in datos_existen:
                existe = False
                for dato_existente in datos_existen:
                    if (
                        dato_existente['tipo'] == dato_nuevo['tipo'] and
                        dato_existente['nSensor'] == dato_nuevo['nSensor'] and
                        dato_existente['valor'] == dato_nuevo['valor']
                    ):
                        existe = True
                        break

                if not existe:
                    datos_existen.append(dato_nuevo)

        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_existen, archivo, indent=4)

    def importar(nombreArchivo):
        with open(nombreArchivo, 'r') as archivo:
            diccionario = json.load(archivo)
        return diccionario
