import questionary
from rich.console import Console

Console().clear()

nombre = questionary.text("¿Cual es tu nombre", default="Miguel").ask()

#Preguntas de selccion multiple
color = questionary.select("¿Cual es tu color favorito?", choices= ["Rojo", "Verde", "Azul", "Otro"],pointer="*").ask()

print(f"Hola, {nombre}! Tu color favorito es {color}.")

if color =="Otro":
    color = questionary.text("¿Cual es tu color favorito?").ask()
    
#Preguntas de confirmacion:    
imprimir = questionary.confirm("¿Quieres imprimir el reusltado?", default=False ).ask()

if imprimir:
    print(f"Hola, {nombre}! tu color favorito es [{color.lower()}]{color}[/].")
else:
    print("Gracias por participar")
        