class NodoDoble:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    @property
    def izquierdo(self):
        return self.anterior

    @izquierdo.setter
    def izquierdo(self, inp):
        self.anterior = inp

    @izquierdo.deleter
    def izquierdo(self):
        del self.anterior

    @property
    def derecho(self):
        return self.siguiente

    @derecho.setter
    def derecho(self, inp):
        self.siguiente = inp

    @derecho.deleter
    def derecho(self):
        del self.siguiente

    def __str__(self):
        return str(self.valor)
