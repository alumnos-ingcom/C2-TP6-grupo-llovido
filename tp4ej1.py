################
# Adrian Evaraldo - @chim20air
# ejercicio 1 - Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """Manejo de error del tipo o rango de entrada"""

    print("Me voy a poner como el de Jurassic Park")
    print(f"Te quedan {cantidad_reintentos} reintentos para poner un entero")
    try:
        entero = int(input(mensaje + ">>> "))
    except ValueError as err:
        if cantidad_reintentos == 0:
            raise IngresoIncorrecto("Volve a primaria pibe") from err
        else:
            entero = ingreso_entero_reintento(mensaje,
                    cantidad_reintentos=cantidad_reintentos-1)
    return entero



def ingreso_entero(mensaje):
    try:
        entero = int(input(mensaje + ">>> "))
    except ValueError:
        entero = ingreso_entero_reintento(f"Pibe te estoy pidiendo un entero")        
    return entero

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    """Funcion para restringir el rango de ingreso"""
    valor = ingreso_entero(mensaje)
    if valor < valor_minimo or valor > valor_maximo:
        raise IngresoIncorrecto(f"el entero tiene que estar entre {valor_minimo} y {valor_maximo}")
    return valor


if __name__ == "__main__":
    print(ingreso_entero("mandale un entero"))
    print(ingreso_entero_restringido("ahora probamos el rango"))
