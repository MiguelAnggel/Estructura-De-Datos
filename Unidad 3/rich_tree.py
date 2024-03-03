from rich import print
from rich.tree import Tree

arbol = Tree("Raiz")

arbol.add("[green]Hijo 1")
arbol.add("[red]Hijo 2")

rama = arbol.add("Hijo 3")
rama.add("hijo 3.1")
rama2 = rama.add("Hijo 3.2")
rama2.add("Hijo 3.2.1")

print(arbol)