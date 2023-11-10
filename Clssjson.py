import json
class Clssjson:

    def exportar_a_json(self, diccionario, arch_nombre="Registro.json"):
        with open(arch_nombre, "w") as archivo:
            json.dump(diccionario, archivo, indent=4)

    def importar_desde_json(self, arch_nombre="Registro.json"):
        try:
            with open(arch_nombre, "r") as archivo:
                diccionario = json.load(archivo)
            return diccionario
        except:
            return []