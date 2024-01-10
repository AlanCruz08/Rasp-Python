from lista import Lista
from Json import ClssJson

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
        ClssJson.guardar(self.Diccionario(), self.archivo)

    def Diccionario(self):
        diccionario_datos = []
        
        for sensor in self.lista:
            diccionario_sensor = {
                'tipo': sensor.get('tipo'),
                'nSensor': sensor.get('nSensor'),
                'valor': sensor.get('valor'),
                'fecha': sensor.get('fecha'),
            }
            diccionario_datos.append(diccionario_sensor)

        return diccionario_datos


if __name__ == '__main__':
    DatosL = DatosArduino()
    DatosL.guardar()
