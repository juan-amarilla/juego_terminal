def ingresar_entero(mensaje: str) -> int:
    """
    Ingresa un numero entero validado.

    Args:
    mensaje(str)

    Returns:
    Retorna el numero entero.
    """

    estado = 0;

    while estado == 0:
       
      try:
         numero = int(input(mensaje))
         estado = 1
    
      except ValueError:
        print("Ingreso un dato no valido. ")

    return numero

def ingresar_nombre(mensaje: str) -> str:
    """
    Ingresa un nombre validado.

    Args:
    mensaje(str).

    Return:
    Retorna el nombre.
    """

    estado = 0

    while estado == 0:
       
      nombre = input(mensaje);
    
      for i in range(len(nombre)):

        if (i + 1) == len(nombre):
          estado = 1
              
        if nombre[i].isspace() == True:
          continue
    
        if nombre[i].isalpha() == True:
          continue
    
        else:
          print(f"Error {mensaje}")
          estado = 0
          break     

    nombre = nombre.title()
    
    return nombre