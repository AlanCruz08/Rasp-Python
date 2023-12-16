import json

class exportarJson:

    """def guardar(diccionario, nombreArchivo="archivo.json"):
        with open(nombreArchivo, 'w') as archivo:
            json.dump(diccionario, archivo, indent=4)"""
    """def guardar(lista_datos, nombre_archivo="archivo.json"):
            datos_exist = []
        
            try:
                #print(lista_datos)
                with open(nombre_archivo, 'r') as archivo:
                    datos_exist = json.load(archivo)
            except:
                pass
            

            lista_datos=lista_datos+datos_exist # Agregar los nuevos datos a los existentes
            lista2=[i for n, i in enumerate(lista_datos) if i not in lista_datos[n + 1:]]
            with open(nombre_archivo, 'w') as archivo:
                json.dump(lista2, archivo, indent=4)"""
    def guardar(datos_nuevos, nombre_archivo="archivo.json"):
        datos_existen = []

        try:
            with open(nombre_archivo, 'r') as archivo:
                datos_existen = json.load(archivo)
        except FileNotFoundError:
            pass

        for dato_nuevo in datos_nuevos:
            if dato_nuevo not in datos_existen:
                # Verifica si el dato ya existe en los datos existentes
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