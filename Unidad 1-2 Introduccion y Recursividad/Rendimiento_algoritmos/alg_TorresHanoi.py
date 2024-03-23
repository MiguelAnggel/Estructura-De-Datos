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
    return (2 ** n) - 1 # Calcular la potencia en python

#VALORES A EVALUAR: 1,5,10,25,50,75,100,250,500,1000
n = 1 #VALOR
#nota: al evaluar 1000 genera error en la version recursiva

for _ in range(10):
    inicio = timeit.default_timer()
    resultado_recursiva = movimientosR(n)
    fin = timeit.default_timer()
    print(f"Tiempo de ejecución (Recursiva): {fin - inicio:.6f} segundos")

    inicio = timeit.default_timer()
    resultado_iteracion = movimientosI(n)
    fin = timeit.default_timer()
    print(f"Tiempo de ejecución (Iteración): {fin - inicio:.6f} segundos")
    print("-" * 40)