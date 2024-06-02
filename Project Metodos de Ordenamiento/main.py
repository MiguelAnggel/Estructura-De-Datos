import random
import time
import timeit
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape
from rich import print
from bubblesort import BubbleSort
from selectionsort import SelectionSort
from quicksort import QuickSort
from heapsort import HeapSort
from radixsort import RadixSort

# Crear un objeto console para usar con Rich
console = Console()
#Genera la lista aleatoria en un rango n entre los numeros 0-50:
def genera_lista_aleatoria(n):
    return [random.randint(0, 50) for _ in range(n)]

#Funcion que hace las mediciones del tiempo de ejecucion de los algoritmos
def medicion_tiempo(sort_function, lista): #sort_function es una funcion de ordenamiento que se aplicara a la lista, sort_function se aplica a la copia de la lista, y el resultado se almacena en lista_ordenada.
    inicio = timeit.default_timer() # timeit Mide el tiempo en milisegundos
    lista_ordenada = sort_function(lista.copy()) #realiza una copia de la lista,asegurandonos que la lista original no se modifique
    fin = timeit.default_timer()
    return fin - inicio, lista_ordenada
'''medicion_tiempo(class1.sort, lista): Llama a la función que mide el tiempo de ordenamiento y
devuelve una tupla con el tiempo y la lista ordenada.'''

#MENU
def main_menu():
#Definimos el siguiente diccionario, asi mismo accedemos a un referencia de las clases creadas(instanciamos)
    algoritmos = {
        1: ("BubbleSort", BubbleSort),
        2: ("SelectionSort", SelectionSort),
        3: ("QuickSort", QuickSort),
        4: ("HeapSort", HeapSort),
        5: ("RadixSort", RadixSort),
    }
    
    while True:
        menu_text = "1.- Ejecutar Algoritmo de Ordenamiento\n2.- Comparar tiempos de ejecución\n3.- Salir"
        console.print(Panel(menu_text, title="[bold magenta]Algoritmos de Ordenamiento[/]", border_style="green"))

        #Manejo de excepciones 
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            console.print("Por favor, ingresa un número válido.", style="bold red")
            continue
        
        if opcion == 1:
            while True:
                print("\n[bold magenta]Algoritmos de Ordenamiento:[/bold magenta]")
                for i in algoritmos:
                    print(f"{i}. {algoritmos[i][0]}")
                
                try:
                    algoritmo_elegido = int(input("Elige el algoritmo a ejecutar: "))
                    if algoritmo_elegido not in algoritmos:
                        console.print("Opción no válida. Inténtalo de nuevo.", style="bold red")
                        continue
                except ValueError:
                    console.print("Por favor, ingresa un número válido.", style="bold red")
                    continue
                
                try:
                    n = int(input("Ingresa el tamaño de la lista N: "))
                except ValueError:
                    console.print("Por favor, ingresa un número válido.", style="bold red")
                    continue
                
                lista = genera_lista_aleatoria(n)
                print(f"\nLista generada aleatoriamente: {lista}")
                algoritmo_nombre, sort_class = algoritmos[algoritmo_elegido]
                print(f"\nEjecutando {algoritmo_nombre}...")
                tiempo_ejecucion, lista_ordenada = medicion_tiempo(sort_class.sort, lista)
                print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} Milisegundos") #Imprime el tiempo de ejecucion con 6c en milisegundos
                print(f"Lista ordenada: {lista_ordenada}")
                
                repetir = input("\n¿Deseas ejecutar otro algoritmo nuevamente? (s/n): ").lower()
                if repetir != 's':
                    break

        elif opcion == 2:
            while True:
                print("\n[bold magenta]Algoritmos de Ordenamiento:[/bold magenta]")
                for i in algoritmos:
                    print(f"{i}. {algoritmos[i][0]}")
                
                try:
                    algoritmo_1 = int(input("Elige el primer algoritmo: "))
                    algoritmo_2 = int(input("Elige el segundo algoritmo: "))
                    if algoritmo_1 not in algoritmos or algoritmo_2 not in algoritmos:
                        console.print("Opción no válida. Inténtalo de nuevo.", style="bold red")
                        continue
                except ValueError:
                    console.print("Por favor, ingresa un número válido.", style="bold red")
                    continue
                
                try:
                    n = int(input("Ingresa el tamaño de la lista N: "))
                except ValueError:
                    console.print("Por favor, ingresa un número válido.", style="bold red")
                    continue
                
                lista = genera_lista_aleatoria(n)
                print(f"\nLista generada aleatoriamente: {lista}")
                nombre1, class1 = algoritmos[algoritmo_1]
                nombre2, class2 = algoritmos[algoritmo_2]
                print(f"\nComparando {nombre1} y {nombre2}...")
                #es una forma de desempaquetado en Python, donde se asignan los valores devueltos por la función medicion_tiempo a las variables tiempo1 y lista_ordenada1.
                '''medicion_tiempo(class1.sort, lista): Llama a la función que mide el tiempo de ordenamiento y
                devuelve una tupla con el tiempo y la lista ordenada.'''
                tiempo1, lista_ordenada1 = medicion_tiempo(class1.sort, lista) #class1.sort: Una referencia al método sort de una clase class1, que es una clase que implementa un algoritmo de ordenamiento (por ejemplo, BubbleSort, QuickSort, etc.).
                tiempo2, lista_ordenada2 = medicion_tiempo(class2.sort, lista)
                print(f"{nombre1} tiempo de ejecución: {tiempo1:.6f} Milisegundos") #Imprime el tiempo de ejecucion con 6c en milisegundos
                print(f"Lista ordenada por {nombre1}: {lista_ordenada1}")
                print(f"{nombre2} tiempo de ejecución: {tiempo2:.6f} Milisegundos")
                print(f"Lista ordenada por {nombre2}: {lista_ordenada2}")
                
                repetir = input("\n¿Deseas comparar otros algoritmos nuevamente? (s/n): ").lower()
                if repetir != 's':
                    break

        elif opcion == 3:
            print("[underline yellow]Saliendo...[/underline yellow]")
            break
        else:
            console.print("Opción no válida. Inténtalo de nuevo.", style="bold red")
        
        # Preguntar al usuario si desea realizar otra operación
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("[underline yellow]Saliendo...[/underline yellow]")
            break

if __name__ == "__main__":
    main_menu()
