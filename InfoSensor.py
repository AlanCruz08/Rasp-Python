from Lista import Lista
import uuid

def get_id():
    return uuid.uuid4()

class InfoSensor(Lista):

    def __init__(self, tipo="", nombre="", unidades=""):
        super().__init__()
        self.id = get_id()
        self.tipo = tipo
        self.nombre = nombre
        self.unidades = unidades
        self.filename = "InfoSensor.json"

    def convertir_a_diccionario(self):
        info_dict = []
        if len(self.lista) > 0 or self.tipo == "":
            for sensor in self.lista:
                info_dict.append(sensor.convertir_a_diccionario())
            return info_dict

        info_dict = {
            "id": self.id,
            "tipo": self.tipo,
            "nombre": self.nombre,
            "unidades": self.unidades
        }

        return info_dict

    def convertir_lista_objeto(self, diccionario):
        for infoSen in diccionario:
            infoSen = self.convertir_objeto(infoSen)
            self.lista.append(infoSen)
        return self

    def convertir_objeto(self, infoSen):
        infoSen = InfoSensor(infoSen["tipo"], infoSen["nombre"], infoSen["unidades"])
        return infoSen

    def cargar(self):
        datos = self.importar_desde_json(self.filename)
        return self.convertir_lista_objeto(datos)

    def guardar(self):
        self.exportar_a_json(self.convertir_a_diccionario(), self.filename)