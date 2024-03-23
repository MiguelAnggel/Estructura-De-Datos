#Algortimos para el calculo del factorial version iterativa
import timeit
#import time

#start = timeit.default_timer()

def factorialI(n):
    
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

#n = 5
#end = timeit.default_timer()
#print(end - start)

#Number es la cantidad de veces que se ejecuta la funcion
print(timeit.timeit(lambda: factorialI(1000), number=10000))

#Tiempo de ejcucion con diferentes valores de n
tiempos = [timeit.timeit(lambda: factorialI(n),number=10000,) for n in range(1,11)]

