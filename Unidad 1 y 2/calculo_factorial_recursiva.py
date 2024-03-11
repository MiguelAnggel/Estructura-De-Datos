#Algoritmo para el calculo del factorial version recursiva
import timeit

def factorialR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorialR(n - 1)
    
def factorialI(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
    
#Number es la cantidad de veces que se ejecuta la funcion
print(timeit.timeit(lambda: factorialR(10), number=10000))#En el argumento de factorial poner num a analizar
# Nota: al evaluar el 1000 exixte fallo en el calculo recursivo

#Tiempo de ejcucion con diferentes valores de n
tiempos = [timeit.timeit(lambda: factorialR(n),number=10000,) for n in range(1,11)]
