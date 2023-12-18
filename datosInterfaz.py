from conexion import ConexionArduino
from datosArduino import DatosArduino
from servidor import mandarDatos
import time
import threading


class DatosInterfaz:
    def __init__(self, conexion):
        self.conexion = conexion
        self.datosArduino = DatosArduino()

    def read_sensor(self, sensor):
        while True:
            arduino_data = self.conexion.leer_dato()
            if arduino_data:
                if arduino_data.startswith(sensor):
                    sensor_values = arduino_data.split(':')
                    if len(sensor_values) >= 2:
                        return sensor_values
                    else:
                        print(
                            f"Error: Datos incompletos recibidos para {sensor}")

    def conexion_servidor(self):
        mandarDatos()
        print("Datos enviados al servidor")

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Sensores ---")
            print("1. Ver Distancia")
            print("2. Ver Movimiento")
            print("3. Ver Humedad")
            print("4. Ver Temperatura")
            print("5. Ver Sonido")
            print("6. Ver todos los datos")
            print("7. Salir")

            opcion = input("Ingrese el número del sensor que desea consultar o '7' para salir: ")

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
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def obtener_todos_los_sensores(self):
        tipos_sensores = ['DIS:', 'SM:', 'SH:', 'ST:', 'SS:']
        stop = False
        try:
            while not stop:
                for tipo_sensor in tipos_sensores:
                    datos_sensor = self.read_sensor(tipo_sensor)
                    if datos_sensor:
                        tipo = datos_sensor[0]
                        nSensor = datos_sensor[1]
                        valor = datos_sensor[2]
                        print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                        datos = {
                            'tipo': tipo,
                            'nSensor': nSensor,
                            'valor': valor,
                        }
                        self.datosArduino.crear(datos)
                self.datosArduino.guardar()
                time.sleep(10)
        except KeyboardInterrupt:
            print("Interrupción del teclado detectada. Saliendo del bucle...")

    def distancia(self):
        while True:
            data = self.read_sensor('DIS:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos = {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
            else:
                print("No hay datos disponibles para el sensor de distancia")

    def movimiento(self):
        while True:
            data = self.read_sensor('SM:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos = {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
            else:
                print("No hay datos disponibles para el sensor de movimiento")
                time.sleep(5)
                break

    def humedad(self):
        while True:
            data = self.read_sensor('SH:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos = {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
            else:
                print("No hay datos disponibles para el sensor de humedad")

    def temperatura(self):
        while True:
            data = self.read_sensor('ST:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos = {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
            else:
                print("No hay datos disponibles para el sensor de temperatura")

    def sonido(self):
        while True:
            data = self.read_sensor('SS:')
            if data:
                tipo = data[0]
                nSensor = data[1]
                valor = data[2]
                print(f"tipo: {tipo}, N° sensor: {nSensor}, Valor: {valor}")
                datos = {
                    'tipo': tipo,
                    'nSensor': nSensor,
                    'valor': valor
                }
                self.datosArduino.crear(datos)
                self.datosArduino.guardar()
            else:
                print("No hay datos disponibles para el sensor de Sonido")


if __name__ == "__main__":
    conexion_arduino = ConexionArduino()
    datos = DatosArduino()

    try:
        sensores = DatosInterfaz(conexion_arduino)
        sensores.mostrar_menu()
        # datos.guardar()

    except KeyboardInterrupt:
        conexion_arduino.cerrar_conexion()
