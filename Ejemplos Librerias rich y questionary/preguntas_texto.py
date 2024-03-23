import questionary
from rich.console import Console
from rich import print

Console().clear()  #Para limpiar la consola

nombre = questionary.text("¿cual es tu nombre?", default="Miguel").ask()
print(f"Hola, {nombre}!")

edad = questionary.text("¿Cuantos años tendras al final de este año?").ask()
edad = int(edad)
print(f"tienes {edad} años.")
año_actual = 2024
año_nacimiento = año_actual - edad
print(f"Naciste en {año_nacimiento}.")

contraseña = questionary.password("Escribe tu contraseña").ask()
print(f"Tu contraseña tiene {len(contraseña)} caracteres.")