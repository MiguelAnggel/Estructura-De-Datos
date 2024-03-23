from nodo import Nodo
class ListaSimple:
    def __init__(self):
        self.cabeza = None   #Cabeza se encuentra vacio(None)
        self.cola = None     #Cola se encuentra vacio(None)
        self.tamaño = 0      #El tamaño de la lista se inicializa en 0
                
    def agregar(self, valor):
        nuevo = Nodo(valor) #Crear un nuevo nodo apuntando a None
        
        if self.cola is None: #Si la lista esta vacia
            self.cabeza = nuevo #el unico elemento
            self.cola = nuevo   #el unico elemento
        else: #Si la lista no esta vacia
            self.cola.siguiente = nuevo   #El siguiente del ultimo que estaba se vulve el nuevo
            
        self.tamaño += 1 #Incrementar el tamaño de la lista
        self.cola = nuevo #Actualizar el ultimo tamaño
        
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.valor == valor:
                if anterior: #No es el primer nodo
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.tamaño -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False 
                        
                
    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, vend=" ->" if actual.siguiente
                  else "\n")
            actual = actual.siguiente
            
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False 
        
            
            
        