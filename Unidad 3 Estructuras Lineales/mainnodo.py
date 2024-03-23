from nodo import Nodo
from lista_simple import ListaSimple

def main():
    ListaSimple()
    
def ejemplo_listasimple():
    lista = ListaSimple()
    
    print("Representacion en memoria:", lista)
    
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)
    
    # 10 -> 20 -> 30 -> None
    
    print("Cabeza:", lista.cabeza.valor)
    print("Cola:", lista.cola.valor)
    
    lista.eliminar(20)
    # 10 -> 30 -> None
    
    lista.recorrer()
    
    print("Siguiente de la cabeza:", lista.cabeza.siguiente.valor)
    
    print(lista.buscar(20)) #TRUE
    print(lista.buscar(40)) #FALSE
    
def nodos():
    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    


if __name__ == "__main__":
    main()