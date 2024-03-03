#Algortimos para el calculo del factorial version iterativa

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
