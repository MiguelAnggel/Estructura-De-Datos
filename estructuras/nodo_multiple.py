from lista_doble import ListaDoble


class NodoMultiple:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = ListaDoble()

    def __str__(self):
        # Si el nodo no tiene hijos, se imprime solo el valor.
        if self.hijos.tamanio == 0:
            return str(self.valor)
        # Si el nodo tiene hijos, se imprime el valor y la lista de hijos.
        else:
            return f"{self.valor}: [{self.hijos}]"