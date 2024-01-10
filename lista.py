class Lista:
    def __init__(self):
        self.lista = []
        self.data = {}

    def crear(self, objeto):
        self.lista.append(objeto)
        self.data = objeto

    def eliminar(self, id):
        objetoEliminar = None
        for objeto in self.lista:
            if objeto.id == id:
                objetoEliminar = objeto
                break
        if objetoEliminar is not None:
            self.lista.remove(objetoEliminar)
        else:
            return f'No se encontro ningun objeto con el id {id}'

    def actualizar(self, id, objeto):
        objetoActualizar = None
        for i, obj in enumerate(self.lista):
            if obj.id == id:
                objetoActualizar = obj
                self.lista[i] = objeto
                break
        if objetoActualizar is None:
            return f'No se encontró ningún objeto con el id {id}'

    def obtener(self):
        return self.lista

    def obtener_por_indice(self, index):
        if 1 <= index <= len(self.lista):
            return self.lista[index - 1]
        else:
            return None
        
    def vaciar(self):
        self.lista.clear()
