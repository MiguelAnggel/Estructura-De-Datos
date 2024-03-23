from rich.console import Console
from rich.table import Table

    
console = Console()

#Titulo de la Tabla:
table = Table(title="Peliculas de Star Wars")
#Añadiendo Columnas:
table.add_column("Episodio", style="cyan", no_wrap=True)
table.add_column("Titulo", style="magenta")
table.add_column("Director", style="green")
#Añadiendo Filas:
table.add_row("IV", "A New Hope", "George Lucas")
table.add_row("V", "The Empire Strikes Back", "Irvin Kershner")
table.add_row("VI", "Return of the Jedi", "Richard Marquand")

console.print(table)