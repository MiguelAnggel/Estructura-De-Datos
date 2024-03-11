class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0
                
    def agregar(self, valor):
        nuevo = None(valor) #Crear un nuevo nodo apuntando a None
        
        if self.cola is None : #Si la lista esta vacia
            self.cabeza = nuevo
            self.cola = nuevo
        else: #Si la lista no esta vacia
            self.cola.siguiente = nuevo
            
        self.tamaño += 1 #Incrementar el tamaño de la lista
        self.cola = nuevo #Actualizar el ultimo tamaño

            
            
        