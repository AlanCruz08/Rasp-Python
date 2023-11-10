from Datos import Datos
from Sensor import Sensor
from Dispositivo import Dispositivo

dato_list = Datos()
dispositivo = Dispositivo("Dispositivo 1")
dispositivo2 = Dispositivo("Dispositivo 2")
dispositivo3 = Dispositivo("Dispositivo 3")

sensor = Sensor("Sensor 1", "Temperatura", 25, dispositivo)
sensor2 = Sensor("", "Temperatura", 25, dispositivo)

