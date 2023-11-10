import uuid

def get_uuid():
    return uuid.uuid4()

class Dispositivo:

    def __init__(self, nombre = "", descripcionDis = ""):
        self.id = get_uuid()
        self.nombre = nombre
        self.descripcionDis = descripcionDis
        