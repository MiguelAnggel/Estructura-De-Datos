import random, os, time
#from colorama import init, Fore, Style

from bubbleSort import bubbleSort # type: ignore
from selectionSort import selectionSort # type: ignore
from quickSort import quickSort # type: ignore
from heapSort import heapSort # type: ignore
from radixSort import radixSort # type: ignore
from ejecutarAlgoritmo import ejecutarAlgoritmo # type: ignore

#init()

def generarLista(N):
    return [random.randint(0, 1000) for _ in range(N)]

# Lista de algoritmos de ordenamiento
algoritmos = [bubbleSort, selectionSort, quickSort, heapSort, radixSort]

# Función para limpiar la pantalla
def limpiarPantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Menú principal
def menu():
    while True:
        limpiarPantalla()
        print("========================")
        print("     PROYECTO FINAL") 
        print("========================")
        print(Fore.BLUE + "PORFAVOR SELECCIONE UN ALGORITMO" + Style.RESET_ALL)
        print(Fore.BLUE + "1. BubbleSort" + Style.RESET_ALL)
        print(Fore.BLUE + "2. SelectionSort" + Style.RESET_ALL)
        print(Fore.BLUE + "3. QuickSort" + Style.RESET_ALL)
        print(Fore.BLUE + "4. HeapSort" + Style.RESET_ALL)
        print(Fore.BLUE + "5. RadixSort" + Style.RESET_ALL)
        print(Fore.BLUE + "6. Comparar tiempos entre 2 algoritmos" + Style.RESET_ALL)
        print(Fore.BLUE + "7. SALIR" + Style.RESET_ALL)

        try:
            opcion = int(input("\nSelecciona un numero del menu: "))
        except ValueError:
            print(Fore.RED + "revise el menu." + Style.RESET_ALL)
            time.sleep(2)
            continue

        if opcion in [1, 2, 3, 4, 5]:
            while True:
                try:
                    N = int(input("\nIntroduce el tamaño de la lista: "))
                except ValueError:
                    print(Fore.RED + "Por favor, introduce un número válido." + Style.RESET_ALL)
                    time.sleep(2)
                    continue
                lista = generarLista(N)
                print(Fore.YELLOW + "\nLista generada al azar:" + Style.RESET_ALL, '\n' + ', '.join(map(str, lista)).center(70))
                tiempo, sorted_list = ejecutarAlgoritmo(algoritmos[opcion - 1], lista)
                print(Fore.GREEN + f"\nTiempo de ejecución del algoritmo seleccionado: {tiempo} segundos" + Style.RESET_ALL)
                print(Fore.YELLOW + "\nLista ordenada con el algorimto:" + Style.RESET_ALL, '\n' + ', '.join(map(str, sorted_list)).center(70))
                repetir = input("\n¿Deseas ejecutar con otro valor de N? (s/n): ").lower()
                if repetir != 's':
                    break
        elif opcion == 6:
            while True:
                try:
                    N = int(input("\nIntroduce el tamaño de la lista: "))
                except ValueError:
                    print(Fore.RED + "Por favor, introduce un número válido." + Style.RESET_ALL)
                    time.sleep(2)
                    continue
                lista = generarLista(N)
                print("\nSelecciona dos algoritmos para comparar:")
                for i, algoritmo in enumerate(algoritmos):
                    print(f"{i + 1}. {algoritmo.__name__}")
                try:
                    seleccion1 = int(input("\nSelecciona el primer algoritmo: "))
                    seleccion2 = int(input("Selecciona el segundo algoritmo: "))
                    algoritmo1 = algoritmos[seleccion1 - 1]
                    algoritmo2 = algoritmos[seleccion2 - 1]
                except (ValueError, IndexError):
                    print(Fore.RED + "Por favor, selecciona dos opciones válidas.".center(70) + Style.RESET_ALL)
                    time.sleep(2)
                    continue
                tiempo1, _ = ejecutarAlgoritmo(algoritmo1, lista[:])
                tiempo2, _ = ejecutarAlgoritmo(algoritmo2, lista[:])
                print(Fore.YELLOW + f"\nTiempo de ejecución de {algoritmo1.__name__}: {tiempo1} segundos" + Style.RESET_ALL)
                print(Fore.YELLOW + f"Tiempo de ejecución de {algoritmo2.__name__}: {tiempo2} segundos" + Style.RESET_ALL)
                time.sleep(5)
                break
        elif opcion == 7:
            break
        else:
            print(Fore.RED + "LA OPCIONES VALIDAS SOLO ESTAN EN EL MENU." + Style.RESET_ALL)
            time.sleep(3)
menu()
#21690067