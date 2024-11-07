from menu import *
from ingresar import *

opcion = 0

while opcion != 3:

    imprimir_menu()
    opcion = ingresar_entero("Ingrese una opcion: ")
    opcion = menu_interaccion(opcion)