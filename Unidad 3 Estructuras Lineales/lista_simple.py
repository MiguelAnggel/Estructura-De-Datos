from nodo import Nodo
class ListaSimple:
    def __init__(self):
        self.cabeza = None   #Cabeza se encuentra vacio(None)
        self.cola = None     #Cola se encuentra vacio(None)
        self.tamanio = 0      #El tamaño de la lista se inicializa en 0
                
    def agregar(self, valor):
        nuevo = Nodo(valor) #Crear un nuevo nodo apuntando a None
        
        if self.cola is None: #Verifica Si la lista esta vacia
            self.cabeza = nuevo #el unico elemento
            self.cola = nuevo   #el unico elemento
        else: #Verifica Si la lista no esta vacia
            self.cola.siguiente = nuevo   #El siguiente del ultimo que estaba se vulve el nuevo
            self.cola = nuevo #Actualizar el ultimo tamaño

        self.tamanio += 1 #Incrementar el tamaño de la lista
        
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.valor == valor:
                if anterior: #No es el primer nodo
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                self.tamanio -= 1
                return True #Valor eliminado
            #Avanza al siguiente nodo
            anterior = actual #El actual se vuelve el "anterior"
            actual = actual.siguiente #El "nuevo actual" es el siguiente
        return False #Valor no encontrado
                        
    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> " if actual.siguiente else "\n")
            actual = actual.siguiente
            
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False 
        