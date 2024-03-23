from rich.console import Console
from rich.table import Table

    
console = Console()

#Titulo de la Tabla:
table = Table(title="Alumnos")
#Añadiendo Columnas:
table.add_column("Numero de control", style= "green")
table.add_column("nombre")
table.add_column("Edad", style="blue")
#Añadiendo Filas:
table.add_row("22690202", "Miguel", "21")
table.add_row("22690066", "spike", "18")
table.add_row("22690160", "zamora", "22")

console.print(table)


