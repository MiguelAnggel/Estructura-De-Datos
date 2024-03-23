# Algoritmo para el problema de las Torres de Hanoi
import timeit  # Libreria para las mediciones de tiempo de ejecucion en milisegundos

#Algoritmo HANOI -- Torres de HANOI version Recursiva:
def movimientosR(n):
    if n == 0:
        return 0
    elif n ==  1:
        return 1
    else:
        return(2*movimientosR(n-1))+1
    
#Algoritmo HANOI -- Torres de HANOI version Iterativa:
def movimientosI(n): 
    return (2 ** n) - 1 # Para Calcular la potencia en python

n = 1 #Valor a evaluar. nota: al evaluar 1000 existe fallo en el recursivo

inicio = timeit.default_timer()
print("Recursivo movimientos", movimientosR(n))
fin = timeit.default_timer()
print("Recursivo tiempo de ejecucion", fin - inicio)

inicio = timeit.default_timer()
print("Iterativo movimientos", movimientosI(n)) 
fin = timeit.default_timer()
print("Iterativo tiempo de ejecucion", fin - inicio)

