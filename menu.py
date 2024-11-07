from juego import *


def imprimir_menu() -> None:
    """
    Imprime un menu

    Args:
    None

    Returns:
    None
    """

    print("El escape de la isla: edicion demo. ")

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
           print(opcion) # otra funcion
               
        
        case 3: 
           print("Gracias por jugar!");

        case _:
           print("Opcion fuera de rango. ") 

    
     return opcion