from Lista import Lista
from Dispositivo import Dispositivo
import uuid

def get_id():
    return uuid.uuid4()

class Sensor(Lista):

    def __init__(self, key = "", read = "", descripcion ="", data = [], device = None):
        self.id = get_id()
        self.key = key
        self.read = read
        self.descripcion = descripcion
        self.data = data
        self.device = device if device else Dispositivo()