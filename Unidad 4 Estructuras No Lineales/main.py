from arbol_binario import ArbolBinario
from nodo_binario import NodoBinario

def main():
    ejemploArbolBinario()


def ejemploArbolBinario():
    arbolVacio = ArbolBinario()
    arbolRaiz = ArbolBinario(10)

    arbolVacio.insertar(8)
    arbolRaiz.insertar(5)


if __name__ == "__main__":
    main()