from listaDoble import ListaDoble
from nodoDoble import NodoDoble

class ListaDobleCircular(ListaDoble):
    def __init__(self):
        super().__init__()

    def agregar_final(self, valor):
        super().agregar_final(valor)
        self.cola.siguiente = self.cabeza
        self.cabeza.anterior = self.cola

    def agregar_inicio(self, valor):
        super().agregar_inicio(valor)
        self.cabeza.anterior = self.cola
        self.cola.siguiente = self.cabeza

    def recorrer_inicio(self):
        actual = self.cabeza  #Mieentras haya un nodo
        #Para que la lista circular no sea infinita
        while actual:
            print(actual.valor, end=" -> " if actual.siguiente else "\n")
            actual = actual.siguiente
            if actual == self.cabeza:
                print() #Para poner una linea en blanco
                break

    def recorrer_fin(self):
        actual = self.cola #Mieentras haya un nodo
        while actual:
            #Para que la lista circular no sea infinita
            print(actual.valor, end=" -> " if actual.anterior else "\n")
            actual = actual.anterior
            if actual == self.cola:
                print()
                break

    def recorrer(self, pasos=1):
        actual = self.cabeza
        for _ in range(pasos): #foe _ in = omite la la variable normalmente utilizada(i), solo sirve para ir pasando
            print(actual.valor, end=" -> ")
            actual = actual.siguiente

    def eliminar_inicio(self):
        if self.cabeza is None:
            return False
        if self.cabeza.siguiente == self.cola: #Si es la misma entonces se desconectan:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza
        self.tamanio -= 1
        return True

    def eliminar_final(self):
        if self.cola is None:
            return False
        if self.cola.anterior == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior #Apuntamos al penultimo
            self.cola.siguiente = self.cabeza #La cola actual apunta a la cabeza de lista
            self.cabeza.anterior = self.cola
        self.tamanio -= 1
        return True
    
    def agregar(self, valor, posicion): # FIXME
        if posicion < 0 or posicion > self.tamanio:
            return False
        if posicion == 0:
            self.agregar_inicio(valor)
        elif posicion == self.tamanio:
            self.agregar_final(valor)
        else:
            nuevo = NodoDoble(valor)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo.anterior = actual.anterior
            nuevo.siguiente = actual
            actual.anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1
            return True
        
    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return False
        if posicion == 0:
            return self.eliminar_inicio()
        elif posicion == self.tamanio -1 :
            return self.eliminar_final()
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamanio -= 1
            return True


