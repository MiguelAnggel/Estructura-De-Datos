from listaDoble import ListaDoble

class Cola(ListaDoble):
    def __init__(self):
        super().__init__()

    def encolar(self, valor):
        super().agregar_final(valor)

    def desencolar(self):
        super().eliminar_inicio()

    def consultar(self):
        if self.cola is not None: #Si cola no es nulo
            return self.cabeza.valor
    
    def esta_vacia(self):
        return self.cabeza is None    #La cabeza(fila esta vacia)
    
    def size(self):
        return self.tamanio
