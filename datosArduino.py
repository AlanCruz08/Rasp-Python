from lista import Lista
from Json import exportarJson
import datetime
import requests
from servidor import mandarDatos


class DatosArduino(Lista):
    def __init__(self, tipo="", nSensor="", valor=""):
        super().__init__()
        self.tipo = tipo
        self.nSensor = nSensor
        self.valor = valor
        self.archivo = "Datos.json"

    def __str__(self):
        if len(self.lista) > 1:
            return f'Contiene {len(self.lista)} elementos'
        return f'{str(self.tipo).ljust(5)} \t\t\t| {self.nSensor.ljust(5)} \t\t\t| {self.valor.ljust(5)}'

    def guardar(self):
        exportarJson.guardar(self.Diccionario(), self.archivo)

        if self.is_connected_to_internet():
            mandarDatos()
            exportarJson.guardar([], self.archivo)

    def is_connected_to_internet(self):
        try:
            requests.get('http://google.com')
            return True
        except requests.exceptions.RequestException as e:
            return False

    def Diccionario(self):
        diccionario_datos = []
        fecha_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for sensor in self.lista:
            datos_sensor = sensor.get('datos', [])
            valor_existente = None

            for dato in datos_sensor:
                if dato['fecha'] == fecha_datetime:
                    valor_existente = dato['valor']
                    break

            if valor_existente is not None:
                diccionario_sensor = {
                    'tipo': sensor.get('tipo'),
                    'nSensor': sensor.get('nSensor'),
                    'valor': valor_existente,
                    'fecha': fecha_datetime
                }
            else:
                diccionario_sensor = {
                    'tipo': sensor.get('tipo'),
                    'nSensor': sensor.get('nSensor'),
                    'valor': sensor.get('valor'),
                    'fecha': fecha_datetime
                }
            diccionario_datos.append(diccionario_sensor)
        return diccionario_datos


if __name__ == '__main__':
    DatosL = DatosArduino()
    DatosL.guardar()
