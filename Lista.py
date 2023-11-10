from Clssjson import Clssjson

class Lista(Clssjson):

    def __init__ (self):
        self.lista =[]
        super().__init__()

    def agregar(self, obj):
        self.lista.append(obj)
    
    def editar(self, index, obj):
        self.lista[index] = obj
    
    def eliminar(self, index):
        self.lista.pop(index)
    
    def regresar_lista(self):
        return self.lista
