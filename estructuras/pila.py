from lista_simple import ListaSimple

class Pila(ListaSimple):
    def __init_subclass__(self):
        super().__init_()

    def apilar(self, valor):
        super().agregar(valor)

    def desapilar(self):
        super().eliminar_final()

    def consultar(self):
        if self.cola is not None: #Verifica que la cola no sea nulo
            return self.cola.valor
        
        return None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def saize(self):
        return self.tamanio
        