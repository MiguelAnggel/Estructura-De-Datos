class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None 
        
    def __str__(self):
        return str(self.valor)