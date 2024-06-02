# Algoritmo de ordenamiento burbuja

'''
Metodo de ordenamiento Burbuja
Revisa cada elemento de la lista con el siguiente elemento,
intercambiandolos de posicion si estan en el orden equivocado

Ejemplo:

4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8 ->En este punto la lista estaria completamente ordenada

'''

class BubbleSort:
    #@staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

