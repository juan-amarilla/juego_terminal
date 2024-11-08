from ingresar import *
from archivos_funciones import agregar_jugador
import random

def evento_aleatorio(eventos: dict) -> int:
    """
    Imprime evento aleatorio

    Args:
    eventos(dict)

    Returns:
    Retorna una cantidad de puntos o retorna numero negativo que seria las heridas
    """

    evento = random.choice(list(eventos.values()))
    print(evento["mensaje"])
    estado = 0

    while estado == 0:

        print("""
        1-Hacer accion!
        2-No hacer accion!
              """)

        opcion = ingresar_entero("Ingrese una opcion: ")

        if opcion == 1:
            resultado = evento["opcion_1"]
            estado = 1

        elif opcion == 2:
            resultado = evento["opcion_2"]
            estado = 1

    return resultado

def lista_eventos() -> dict:
    """
    es un diccionario de eventos

    Args:
    None

    Returns:
    Retorna el diccionario de eventos
    """

    eventos = {

        "evento_1": {"mensaje": "Encontro una estatua lo investigara o se ira? ", 
                     "opcion_1": 50, 
                     "opcion_2": 25},

        "evento_2": {"mensaje": "Encontro un campamento lo investigara o se ira? ", 
                     "opcion_1": 25, 
                     "opcion_2": 25},

        "evento_3": {"mensaje": "Encontro una escritura rara lo analizara mas cerca o no lo hara? ", 
                     "opcion_1": 45, 
                     "opcion_2": 25},

        "evento_4": {"mensaje": "Encontro una vibora atacara o huira? ", 
                     "opcion_1": 25, 
                     "opcion_2": -25},

        "evento_5": {"mensaje": "Encontro una losa de piedra lo recogera o lo dejara en el suelo? ", 
                     "opcion_1": 50, 
                     "opcion_2": 25},

        "evento_6": {"mensaje": "Encontro un ??? atacara o huira? ", 
                     "opcion_1": -75, 
                     "opcion_2": 25},

        "evento_7": {"mensaje": "Encontro un animal no identificado atacara o huira? ", 
                     "opcion_1": 10, 
                     "opcion_2": 10}
    }

    return eventos

def obtener_puntos(sobrevivir, jugador) -> dict:
    """
    Se obtendra puntos

    Args:
    None

    Returns:
    Retorna el diccionario de eventos
    """

    if sobrevivir == 20:
        jugador["puntos"] = jugador["puntos"] * sobrevivir
        print("Logro sobrevivir y escapo con exito vino un barco de casualidad y logro escapar!!")
        print(f"Puntos finales del jugador {jugador['nombre']}: {jugador['puntos']}")

    else:
        jugador["puntos"] = jugador["puntos"] * sobrevivir
        print("Perdio, gracias por jugar esta partida!!")
        print(f"Puntos finales del jugador {jugador['nombre']}: {jugador['puntos']}")

    return jugador


def comenzar_juego() -> None:
    """
    Se comienza el juego

    Args:
    None

    Returns:
    None
    """

    nombre = ingresar_nombre("Ingrese como se llama su jugador: ")
    jugador = {"nombre": nombre, "salud": 100, "puntos": 0}
    lista = []
    sobrevivir = 0
    estado = 0
    
    eventos = lista_eventos()

    while estado == 0:

        resultado = evento_aleatorio(eventos)

        print(f"el resultado {resultado}")

        if resultado > 0:
            jugador["puntos"] += resultado
            print(f"Obtuvo {resultado} puntos! ")
            print(f"Sus puntos: {jugador['puntos']}.")

        else:
            jugador["salud"] += resultado
            print(f"le hicieron {resultado} de herida cuidado! ")
            print(f"Su salud actual: {jugador['salud']}.")

        if sobrevivir == 20 or jugador["salud"] <= 0:
            estado = 1
            break

        sobrevivir += 1
        print(f"dias sobrevividos: {sobrevivir}")

    jugador = obtener_puntos(sobrevivir, jugador)
    
    lista.append(jugador["nombre"])
    lista.append(jugador["puntos"])

    agregar_jugador("jugadores.txt", lista)