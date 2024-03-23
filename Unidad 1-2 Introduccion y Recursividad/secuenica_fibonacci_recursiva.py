#Algoritmo de la secuencia fibonacci en version recursiva:
import timeit

def fibonacciR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciR(n - 1) + fibonacciR(n - 2)

#Ejemplo de uso:  
n = 5 #Valores a evaluar
inicio = timeit.default_timer()
fin = timeit.default_timer()
print("Recursivo tiempo de ejecucion", fin - inicio)
