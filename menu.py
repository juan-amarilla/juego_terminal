"""
Módulo que maneja la interacción con el menú del juego.

Este módulo proporciona las funciones para mostrar un menú al jugador y gestionar
las opciones seleccionadas, como comenzar el juego, mostrar las puntuaciones o salir.

Funciones:
    - imprimir_menu(): Muestra las opciones del menú al jugador.
    - menu_interaccion(opcion: int): Procesa la opción seleccionada por el jugador
      y ejecuta la acción correspondiente.

Dependencias:
    - comenzar_juego: Función para iniciar una nueva partida.
    - leer_jugadores: Función para mostrar las puntuaciones guardadas.
"""
from juego import comenzar_juego
from archivos_funciones import leer_jugadores


def imprimir_menu() -> None:
    """
    Imprime un menu

    Args:
    None

    Returns:
    None
    """

    print("\n--- Comienza la aventura en la Isla Perdida ---")

    print("""
    1-Jugar.
    2-Mostrar puntuaciones.
    3-Salir.
    """)


def menu_interaccion(opcion: int) -> int:
    """
    Seleccionas una opcion del menu

    Args:
    opcion(int)

    Returns:
    Retorna la opcion elegida
    """

    match opcion:

        case 1:
            comenzar_juego()

        case 2:
            print("\n--- Puntuaciones ---")
            leer_jugadores("jugadores.txt")

        case 3:
            print("Gracias por jugar!")

        case _:
            print("Opcion fuera de rango. ")

    return opcion
