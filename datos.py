from conexion import ConexionArduino
import time
from datosArduono import Datos
from servidor import mandarDatos
#import datetime




class SensoresArduino:
    def __init__(self, conexion):
        self.conexion = conexion
        self.datosArduino = Datos()
    
    def read_sensor(self, sensor):
        while True:
            arduino_data = self.conexion.leer_dato()
            if arduino_data:
                if arduino_data.startswith(sensor):
                    sensor_values = arduino_data.split(':')
                    if len(sensor_values) >= 2:
                        #self.datosArduino.guardar()
                        return sensor_values
                    else:
                        print(f"Error: Datos incompletos recibidos para {sensor}")
            

     
    """def buscar_sensor(self, datos_arduino, tipo, sensores_vistos, nSensor, valor):
        sensor_encontrado = next((sensor for sensor in datos_arduino if tipo == sensor.sku ), None)
        if sensor_encontrado == next((sensor for sensor in datos_arduino if tipo == sensor.sku ), None):
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtener la fecha y hora actual
            print(f"SKU: {sensor_encontrado.sku} \t\t N Sensor: {nSensor} \t\t Valor: {valor} \t\t Nombre: {sensor_encontrado.nombre} \t\t Unidad: {sensor_encontrado.unidad}")
            sensores_vistos.add(sensor_encontrado)
            guardar_sensor = {
                    "SKU": tipo,
                    "N Sensor": nSensor,
                    "Valor": valor,
                    "Nombre": sensor_encontrado.nombre,
                    "Unidad": sensor_encontrado.unidad,
                    "Fecha": fecha_actual
                }
            self.SensorDatos.guardar(guardar_sensor, "Datos.json")
            
        return sensor_encontrado if sensor_encontrado else None"""
        
    def conexion_servidor(self):
        mandarDatos()



    
    def distancia(self):
        #sku = self.SensoresData.obtener_Sensores()
        sensores_vistos = set()  # Almacena los sensores ya mostrados

        while True:
            data = self.read_sensor('DIS:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos =  {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                
                #self.buscar_sensor(sku, tipo, sensores_vistos, nSensor, valor)
            else:
                print("No hay datos disponibles para el sensor de distancia")
    

    def movimiento(self):
        #sku = self.SensoresData.obtener_Sensores()
        sensores_vistos = set()  # Almacena los sensores ya mostrados

        while True:
            data = self.read_sensor('SM:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos =  {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                #self.buscar_sensor(sku, tipo, sensores_vistos, nSensor, valor)
                
                
            else:
                print("No hay datos disponibles para el sensor de movimiento")
                time.sleep(5)
                break 
        #guardarSensor = sensor_encontrado.Diccionario()
        #self.SensorDatos.guardar(guardarSensor, "Datos.json")
        


    def humedad(self):
        #sku = self.SensoresData.obtener_Sensores()
        sensores_vistos = set()  # Almacena los sensores ya mostrados

        while True:
            data = self.read_sensor('SH:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos =  {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                #self.buscar_sensor(sku, tipo, sensores_vistos, nSensor, valor)
            else:
                print("No hay datos disponibles para el sensor de humedad")

    def temperatura(self):
        #sku = self.SensoresData.obtener_Sensores()
        sensores_vistos = set()  # Almacena los sensores ya mostrados

        while True:
            data = self.read_sensor('ST:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos =  {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                #self.buscar_sensor(sku, tipo, sensores_vistos, nSensor, valor)
            else:
                print("No hay datos disponibles para el sensor de temperatura")
    
    
    def sonido(self):
        #sku = self.SensoresData.obtener_Sensores()
        sensores_vistos = set()  # Almacena los sensores ya mostrados

        while True:
            data = self.read_sensor('SS:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos =  {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                #self.buscar_sensor(sku, tipo, sensores_vistos, nSensor, valor)
            else:
                print("No hay datos disponibles para el sensor de Sonido")

    


    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Sensores ---")
            print("1. Ver Distancia")
            print("2. Ver Movimiento")
            print("3. Ver Humedad")
            print("4. Ver Temperatura")
            print("5. Ver Sonido")
            print("6. Ver todos los datos")
            print("7. Enviar datos al servidor")
            print("8. Salir")

            opcion = input("Ingrese el número del sensor que desea consultar o '8' para salir: ")

            if opcion == '1':
                self.distancia()
                
            elif opcion == '2':
               self.movimiento()
            elif opcion == '3':
                self.humedad()
            elif opcion == '4':
               self.temperatura()
            elif opcion == '5':
                self.sonido()
            elif opcion == '6':
                while True:
                    self.obtener_todos_los_sensores()
                    break
            elif opcion == '7':
                self.conexion_servidor()
                break
            elif opcion == '8':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def obtener_todos_los_sensores(self):
        
        sensores_vistos = set()
        #sku = self.SensoresData.obtener_Sensores()

        tipos_sensores = ['DIS:', 'SM:', 'SH:', 'ST:', 'SS:']
        while True:
            for tipo_sensor in tipos_sensores:
                datos_sensor = self.read_sensor(tipo_sensor)
                if datos_sensor:
                    tipo = datos_sensor[0]
                    nSensor = datos_sensor[1]
                    valor = datos_sensor[2]
                    print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                    datos =  {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor,
                    
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                    #self.buscar_sensor(sku, tipo, sensores_vistos, nSensor, valor)


"""if __name__ == "__main__":
    conexion_arduino = ConexionArduino()
    datos = Datos()

    try:
        sensores = SensoresArduino(conexion_arduino)
        sensores.obtener_todos_los_sensores()
        sensores.mostrar_menu()
        datos.guardar()
        
    except KeyboardInterrupt:
        conexion_arduino.cerrar_conexion()"""

if __name__ == "__main__":
    conexion_arduino = ConexionArduino()
    datos = Datos()

    try:
        sensores = SensoresArduino(conexion_arduino)
        sensores.mostrar_menu()
        datos.guardar()
        
    except KeyboardInterrupt:
        conexion_arduino.cerrar_conexion()





