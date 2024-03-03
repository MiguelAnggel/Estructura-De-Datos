import timeit  # Libreria para las mediciones de tiempo de ejecucion en milisegundos
#import time #Mide el tiempo de ejecucion en segundos

#Algoritmo HANOI -- Torres de HANOI version recursiva
def movimientos(): 
    return (2 ** n) - 1 # Calcular la potencia en python

def movimientosR(n):
    if n == 0:
        return 0
    elif n ==  1:
        return 1
    else:
        return(2*movimientosR(n-1))+1

n = 100

inicio = timeit.default_timer()
print("No recursivo", movimientos()) #Aqui en el argumento quite n, despues de eso funciono 
fin = timeit.default_timer()
print("No recursivo", fin - inicio)


inicio = timeit.default_timer()
print("Recursivo", movimientosR(n))
fin = timeit.default_timer()
print("Recursivo", fin - inicio)