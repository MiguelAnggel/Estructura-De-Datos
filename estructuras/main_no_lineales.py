from arbol_binario import ArbolBinario

def main():
    ejemploArbolBinario()


def ejemploArbolBinario():
    # arbolVacio = ArbolBinario()
    arbolRaiz = ArbolBinario(10)

    # arbolVacio.insertar(5)
    # arbolVacio.insertar(7)

    arbolRaiz.insertar(8)
    arbolRaiz.insertar(20)
    arbolRaiz.insertar(5)
    arbolRaiz.insertar(9)
    arbolRaiz.insertar(23)
    arbolRaiz.insertar(15)

    '''print("Preorden")
    arbolRaiz.preorden()

    print("Inorden")
    arbolRaiz.inorden()

    print("Postorden")
    arbolRaiz.postorden()'''

    arbolRaiz.insertar(17)
    arbolRaiz.insertar(7)
    arbolRaiz.insertar(24)
    arbolRaiz.insertar(22)
    arbolRaiz.insertar(4)

    print("===")
    print("15 esta en el árbol:", arbolRaiz.buscar(15))
    print("7 esta en el árbol:", arbolRaiz.buscar(7))
    print(f"Anchura: {arbolRaiz.anchura(debug=True)}" f"\tAltura: {arbolRaiz.altura()}")



if __name__ == "__main__":
    main()