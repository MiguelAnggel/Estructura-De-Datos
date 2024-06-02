import time

def ejecutarAlgoritmo(algoritmo, lista):
    inicio = time.time()
    sorted_list = algoritmo(lista[:])  # Usamos una copia de la lista para evitar efectos colaterales
    fin = time.time()
    return fin - inicio, sorted_list
