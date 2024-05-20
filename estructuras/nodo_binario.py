from nodo_doble import NodoDoble


class NodoBinario(NodoDoble):
    def __init__(self, valor):
        super().__init__(valor)

    def conexiones(self):
        if self.izquierdo is not None and self.derecho is not None:
            return f'({self.izquierdo.valor} <- {self.valor} -> {self.derecho.valor})'
        elif self.izquierdo is not None:
            return f'({self.izquierdo.valor} <- {self.valor})'
        elif self.derecho is not None:
            return f'({self.valor} -> {self.derecho.valor})'
        else:
            return str(self.valor)