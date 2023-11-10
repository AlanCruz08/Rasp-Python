from Lista import Lista
from Dispositivo import Dispositivo
import uuid

def get_id():
    return uuid.uuid4()

class Sensor(Lista,Dispositivo):

    def __init__(self, key = "", type = "", read = "", units = "", description = "", device = None):
        super().__init__()
        self.id = get_id()
        self.key = key
        self.type = type
        self.read = read
        self.units = units
        self.descrption = description
        self.device = device if device else Dispositivo()