from nodo import Nodo
from lista_simple import ListaSimple
from listaDoble import ListaDoble
from listadobleCircular import ListaDobleCircular as ListaCircular #Le ponemos un alias corto

# def main() -> para ejecutar sola una instancia y sus metodos
def main():
    ejemploListaCircular()

def ejemploListaSimple():
    lista = ListaSimple()

    print("Representación en memoria:", lista)

    lista.agregar(10)
    lista.agregar(30)
    lista.agregar(50)

    print("Cabeza:", lista.cabeza.valor)
    print("Cola:", lista.cola.valor)

    lista.recorrer()

    lista.eliminar(30)
    lista.recorrer()

    print("Buscar 30: ", lista.buscar(30))
    print("Buscar 10: ", lista.buscar(10))

def ejemploListaDoble():
    lista = ListaDoble()
    lista.recorrer_inicio()

    lista.agregar_final(10)  # 10
    lista.agregar_inicio(20)  # 20 <-> 10
    lista.agregar(30)  # 20 <-> 10 <-> 30
    lista.agregar(40)  # 20 <->10 <-> 30 <-> 40
    lista.agregar(50)  # 20 <->10 <-> 30 <-> 40 <-> 50
    lista.recorrer_inicio()
    lista.recorrer_fin()

    print("Eliminaciones")
    lista.eliminar_inicio()  # 10 <-> 30 <-> 40 <-> 50
    lista.recorrer_inicio()
    lista.eliminar_final()  # 10 <-> 30 <-> 40
    lista.recorrer_inicio()
    lista.eliminar(10)  # 30 <-> 40
    lista.recorrer_inicio()

    lista.agregar_inicio(30)
    lista.agregar_inicio(40)
    lista.recorrer_inicio()

    print("Buscar 30:", lista.buscar(30))
    print("Buscar 75:", lista.buscar(75))

def ejemploListaCircular():
    lista = ListaCircular
    lista.recorrer_inicio()

    lista.agregar_inicio(100)
    lista.agregar_inicio(200)
    #lista.recorrer_inicio()
    lista.agregar_final(250)
    lista.agregar_inicio(300)
    lista.agregar_final(400)
    print("Elementos de la lista circular")
    lista.recorrer_inicio()
    #lista.recorrer_fin()
    #lista.recorrer(7)
    print("Eliminaciones")
    for _ in range(lista.tamanio):
        lista.eliminar_inicio()
        lista.recorrer_inicio()

def nodos():
    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3

if __name__ == "__main__":
    main()