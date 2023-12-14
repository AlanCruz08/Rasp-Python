from listaMetodos import Lista
from Json import exportarJson
import datetime

class Datos(Lista):
    def __init__(self,tipo="", nSensor="", valor= ""):
        super().__init__()
        self.tipo = tipo
        self.nSensor = nSensor
        self.valor = valor
        self.archivo = "Datos.json"
        
        

    def __str__(self):
        if len(self.lista)>1:
            return f'Contiene {len(self.lista)} elementos'
        return f'{str(self.tipo).ljust(5)} \t\t\t| {self.nSensor.ljust(5)} \t\t\t| {self.valor.ljust(5)}'

    def guardar(self):
        exportarJson.guardar(self.Diccionario(),self.archivo)
             
    
    #def convertirJson(self,lista):
        #print("funciones: ", lista)
         
     #   for datos in lista:
      #      id = datos.get('id')
       #     puertos = datos.get('puertos')
        #    descripcion = datos.get('descripcion')
         #   sensorDatos = Datos(id,puertos,descripcion)
          #  self.crear(sensorDatos)
    
    #def importar(self):
     #       Dic = exportarJson.importar(self.archivo)
      #      self.convertirJson(Dic)
            
    
    """def Diccionario(self):
        diccionario_datos = []
        #print(self.lista)
       
        for sensor in self.lista:
                    #print(sensor)
                    
            diccionario_sensor = {
                'tipo': sensor.get('tipo'),
                'nSensor': sensor.get('nSensor'),
                'valor': sensor.get('valor'),           
                }
            diccionario_datos.append(diccionario_sensor)
        return diccionario_datos"""
    def Diccionario(self):
        diccionario_datos = []
        fecha_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Convertir la fecha a datetime

        for sensor in self.lista:
            datos_sensor = sensor.get('datos', [])
            valor_existente = None

            # Buscar si ya existe un dato para esa fecha y ese sensor
            for dato in datos_sensor:
                if dato['fecha'] == fecha_datetime:
                    valor_existente = dato['valor']
                    break

            # Si hay un valor existente para esa fecha, actualiza el valor
            if valor_existente is not None:
                diccionario_sensor = {
                    'tipo': sensor.get('tipo'),
                    'nSensor': sensor.get('nSensor'),
                    'valor': valor_existente,  # Utiliza el valor existente
                    'fecha': fecha_datetime  # Agrega la fecha al diccionario como datetime
                }
            else:
                # Si no existe un valor para esa fecha, agrega uno nuevo
                diccionario_sensor = {
                    'tipo': sensor.get('tipo'),
                    'nSensor': sensor.get('nSensor'),
                    'valor': sensor.get('valor'),
                    'fecha': fecha_datetime  # Agrega la fecha al diccionario como datetime
                }

            diccionario_datos.append(diccionario_sensor)

        return diccionario_datos

if __name__ == '__main__':
     
    DatosL = Datos()
    DatosL.guardar()