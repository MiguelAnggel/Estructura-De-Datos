from nodoDoble import NodoDoble

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def agregar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.cola is None:  # Si la lista está vacía
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1

    def agregar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar(self, valor):
        self.agregar_final(valor)

    def eliminar_inicio(self):
        if self.cabeza is None:
            return False

        if self.cabeza.siguiente is None:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self.tamanio -= 1

        return True

    def eliminar_final(self):
        if self.cola is None:
            return False

        if self.cola.anterior is None:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self.tamanio -= 1

        return True

    def eliminar(self, valor):
        actual = self.cabeza

        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior

                self.tamanio -= 1
                return True

            actual = actual.siguiente
        return False

    def recorrer_inicio(self):
        if self.cabeza is None:
            print("[]")
            return False

        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> " if actual.siguiente else "\n")
            actual = actual.siguiente

        return True

    def recorrer_fin(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" <- " if actual.anterior else "\n")
            actual = actual.anterior

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False