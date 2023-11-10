import serial
class Ard:
    def leer(self):
        arduino_port = '/dev/ttyUSB0'
        baud_rate = 9600
        ser = serial.Serial(arduino_port, baud_rate)
        try:
            while True:
                data = ser.readline().decode().strip()
                print("Distancia desde el sensor ultrasónico:", data, "cm")
        except KeyboardInterrupt:
            ser.close()