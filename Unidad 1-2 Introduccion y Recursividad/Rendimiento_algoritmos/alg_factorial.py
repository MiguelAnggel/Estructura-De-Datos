#Programa para el calculo del factorial en version Recursiva e Iterativa 
import timeit #Libreria para calcular el tiempo de ejecucion en milisegundos

#Version Recurisva:
def factorialR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorialR(n - 1)
    
#Version Iterativa:
def factorialI(n):
    
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
    
# VALORES A EVALUAR: 1,5,10,25,50,75,100,250,500,100
n = 1 #Valor 
'''Nota: En la ejecucion del valor 1000 en la version recursiva sobrepasa el limite
Es decir generara error.'''

for _ in range(10):
    inicio = timeit.default_timer()
    resultado_recursiva = factorialR(n)
    fin = timeit.default_timer()
    print(f"Tiempo de ejecución (Recursiva): {fin - inicio:.6f} segundos")

    inicio = timeit.default_timer()
    resultado_iteracion = factorialI(n)
    fin = timeit.default_timer()
    print(f"Tiempo de ejecución (Iteración): {fin - inicio:.6f} segundos")
    print("-" * 40)