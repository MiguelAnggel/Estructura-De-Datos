from rich import print
from rich.console import Console
import questionary

console = Console()

console.clear()

tamaño = questionary.select("¿Cual es el tamaño de tu pizza?", choices=["Chica", "Mediana", "Grande"]).ask()


ingredientes = questionary.checkbox("Que ingredientes quieres en tu pizza?", choices=["Pepperoni", "Jamon", "Pimienta", "Queso extra"], pointer ="*").ask()

print(f"Tu pizza {tamaño.lower()} con {','.join(ingredientes)} esta en camino!")

