from nodo_binario import NodoBinario

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

    #funcion privada
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
        

