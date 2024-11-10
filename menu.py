from juego import *
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
