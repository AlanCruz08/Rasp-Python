import serial

class ConexionArduino:
    def __init__(self, arduino_port='COM3', baud_rate=9600):
        self.ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    
    def leer_dato(self):
        if self.ser.in_waiting > 0:
            return self.ser.readline().decode('utf-8').rstrip()

    def cerrar_conexion(self):
        self.ser.close()