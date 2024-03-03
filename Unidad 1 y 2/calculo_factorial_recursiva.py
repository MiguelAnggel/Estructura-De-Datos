#Algoritmo para el calculo del factorial version recursiva
import timeit

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n -1)
    
#Number es la cantidad de veces que se ejecuta la funcion
print(timeit.timeit(lambda: factorial(10), number=10000))

#Tiempo de ejcucion con diferentes valores de n
tiempos = [timeit.timeit(lambda: factorial(n),number=10000,) for n in range(1,11)]