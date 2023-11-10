import serial
import uuid
from Lista import Lista
from Sensor import Sensor

def get_id():
    return uuid.uuid4()

class Datos(Lista):

    def __init__(self, nombre = "", hora = "", fecha = "", valor = 0, unidades = "", sensor = None):
        super().__init__()
        self.id = get_id()
        self.nombre = nombre
        self.valor = valor
        self.fecha = fecha
        self.hora = hora
        self.sensor = sensor if sensor else Sensor()
        self.filename = "Datos.json"
    
    def leerdatos(self):
        pass 
    
    def mostrar(self):
        if len(self.lista) > 1:
            cadena = "Index \t\t\t Valor \t\t\t Unidades \t\t\t Hora \t\t\t Fecha \n"
            for index, funcion in enumerate(self.lista):
                cadena += f"{index} \t\t\t {funcion.mostrar()}\n"
            return cadena
        return f"{self.valor} \t\t\t {self.unidades} \t\t\t {self.hora} \t\t\t {self.fecha}"

    def __str__(self):
        if len(self.lista) > 1:
            return f"Contiene {len(self.lista)} Datos"
        return f"Valor: {self.valor}, Unidades: {self.unidades}, Hora: {self.hora}, Fecha: {self.fecha}"
    
    def com_arduino(self):
        arduino = serial.Serial('COM3', 9600)
        return arduino