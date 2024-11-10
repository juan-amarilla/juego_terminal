"""
Módulo principal que maneja la interacción del jugador con el menú del juego.

Este módulo gestiona el flujo principal del juego, donde se muestra un menú al jugador,
se recibe su opción de entrada y se ejecuta la acción correspondiente (iniciar el juego,
mostrar puntuaciones o salir).

Funciones:
    - No se definen funciones en este módulo, pero se importa y utiliza:
      - imprimir_menu: Muestra las opciones del menú.
      - menu_interaccion: Procesa la opción seleccionada y ejecuta la acción correspondiente.

Dependencias:
    - menu: Módulo que contiene las funciones de interacción con el menú.
    - ingresar: Módulo que proporciona la función para ingresar un número entero.
    
El ciclo continúa hasta que el jugador elige salir, es decir, cuando selecciona la opción 3.
"""

from menu import menu_interaccion, imprimir_menu
from ingresar import ingresar_entero

OPCION = 0

while OPCION != 3:

    imprimir_menu()
    opcion = ingresar_entero("Ingrese una opcion: ")
    OPCION = menu_interaccion(opcion)
