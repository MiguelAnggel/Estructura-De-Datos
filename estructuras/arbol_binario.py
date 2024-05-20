from nodo_binario import NodoBinario
from cola import Cola

class ArbolBinario:

# Constructor arbol Vacio (iniciar el arbol vacio)
    #def __init__(self):
        #self.raiz = None
        #self.tamanio = 0

#Constructor arbolo con raiz (iniciar el arbol con raiz)
    def __init__(self, raiz):
        if raiz is None:
            self.raiz = None
            self.tamanio = 0
        else:
            self.raiz = NodoBinario(raiz)
            self.tamanio = 1

    def insertar(self, valor):
        nuevo_nodo = NodoBinario(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self.__insertar(self.raiz, nuevo_nodo)

        self.tamanio += 1

    def __insertar(self, nodo, nuevo_nodo):
        if nuevo_nodo.valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = nuevo_nodo
            else:
                self.__insertar(nodo.izquierdo, nuevo_nodo)
        else:
            if nodo.derecho is None:
                nodo.derecho = nuevo_nodo
            else:
                self.__insertar(nodo.derecho, nuevo_nodo)

    def eliminar(self, valor):
        if self.raiz is not None:
            self.raiz = self.__eliminar(self.raiz, valor)
            self.tamanio -= 1

    def __eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierdo = self.__eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self.__eliminar(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

    def preorden(self):
        self.__preorden(self.raiz)

    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self.__preorden(nodo.izquierdo)
            self.__preorden(nodo.derecho)

    def inorden(self):
        self.__inorden(self.raiz)

    def __inorden(self, nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierdo)
            print(nodo.valor)
            self.__inorden(nodo.derecho)

    def postorden(self):
        self.__postorden(self.raiz)

    def __postorden(self, nodo):
        if nodo is not None:
            self.__postorden(nodo.izquierdo)
            self.__postorden(nodo.derecho)
            print(nodo.valor)

    def buscar(self, valor):
        return self.__buscar(self.raiz, valor)

    def __buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self.__buscar(nodo.izquierdo, valor)
        else:
            return self.__buscar(nodo.derecho, valor)

    def altura(self):
        return self.__altura(self.raiz)

    def __altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.__altura(nodo.izquierdo), self.__altura(nodo.derecho))

    def anchura(self, nodo=None, debug=False):
        if nodo is None:
            return self.__anchura(self.raiz, debug=debug)
        else:
            return self.__anchura(nodo, debug=debug)

    def __anchura(self, nodo, debug=False):
        if nodo is None:
            return 0

        cola = Cola()
        cola.encolar(nodo)

        max_ancho = 0
        nivel_ancho = 1  # Anchura de la raíz
        nivel = 1

        while cola.esta_vacia() is False:
            # Procesa todos los nodos en el nivel actual (ancho)
            if debug:
                print(f"Nivel: {nivel}\tAncho: {nivel_ancho}")

            # cola.recorrer_inicio()

            for _ in range(cola.size()):
                if cola.esta_vacia():  # Si la cola está vacía,
                    break

                actual = cola.desencolar()  # Obtiene el primer nodo de la cola
                if debug:
                    print(actual.conexiones())

                # Agregar hijos a la cola para el siguiente nivel
                if actual.izquierdo:
                    cola.encolar(actual.izquierdo)
                if actual.derecho:
                    cola.encolar(actual.derecho)

            # Actualizar max_ancho si el nivel actual tiene más nodos
            if cola.size() > max_ancho:
                max_ancho = cola.size()

            # Calcula el ancho para el siguiente nivel
            nivel_ancho = cola.size()
            nivel += 1

        return max_ancho

    def __str__(self):
        return str(self.raiz)