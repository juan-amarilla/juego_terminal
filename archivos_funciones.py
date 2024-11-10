"""
Este módulo contiene funciones relacionadas con la gestion de jugadores, como agregar jugadores
a un archivo
"""


def agregar_jugador(ruta: str, lista: list) -> None:
    """ 
    Agregas un jugador en el archivo

    Args:
    ruta(str)
    lista(list)

    Returns:
    None
    """

    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(str(lista) + "\n")


def leer_jugadores(ruta: str) -> None:
    """
    Lee el archivo de jugadores

    Args:
    ruta(str)

    Returns:
    None
    """

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_sin_corchetes = linea.replace(
                "[", "").replace("]", "").strip()
            print(linea_sin_corchetes)
