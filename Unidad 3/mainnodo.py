from nodo import Nodo

def main():
    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    


if __name__ == "__main__":
    main()