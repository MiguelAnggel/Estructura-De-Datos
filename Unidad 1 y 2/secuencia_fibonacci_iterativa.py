#Algoritmo para el calculo de la secuencia fibonacci en forma Iterativa:
import timeit

def fibonacci_iterativo(n):
    if n <= 0:
        return "El valor de 'n' debe ser mayor que cero."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Ejemplo de uso:
n = 10
resultado = fibonacci_iterativo(n)
print(f"Los primeros {n} términos de la secuencia de Fibonacci son: {resultado}")
print("\n")
inicio = timeit.default_timer()
fin = timeit.default_timer()
print("iterativo tiempo de ejecucion", fin - inicio)