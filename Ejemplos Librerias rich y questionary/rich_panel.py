from rich.console import Console
from rich.panel import Panel

console = Console()

panel1 = Panel.fit("HOLA")
panel2 = Panel("HOLA")

panel3 = Panel.fit("[green]Hola[/green] [blue]mundo[/blue]", title="panel 3", border_style="#ffa500")

console.print(panel1, panel2, panel3, sep="\n")