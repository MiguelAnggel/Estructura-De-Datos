#Algoritmos para la sucesion fibonacci 
import timeit

#Fibonacci version Recursiva:
def fibonacci_recursiva(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursiva(n - 1) + fibonacci_recursiva(n - 2)

#Fibonacci version Iterativa:
def fibonacci_iterativa(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# VALORES A EVALUAR: 1,5,10,25,50,75,100,250,500,100
n = 1 #Valor
'''Nota: En la ejecucion del valor 1000 en la version recursiva sobrepasa el limite
Es decir generara error.'''

for _ in range(10):
    inicio = timeit.default_timer()
    resultado_recursiva = fibonacci_recursiva(n)
    fin = timeit.default_timer()
    print(f"Tiempo de ejecución (recursiva): {fin - inicio:.6f} segundos")

    inicio = timeit.default_timer()
    resultado_iteracion = fibonacci_iterativa(n)
    fin = timeit.default_timer()
    print(f"Tiempo de ejecución (Iteración): {fin - inicio:.6f} segundos")
    print("-" * 40)
    
