################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 5 - Decodificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp5ej8 import decodificado_cesar
from time import sleep


class FileNotFoundError(Exception):
    ''' Error que genera cuando no se encuentra el archivo.'''
    pass



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def decodificacion(file, file_copy, rotate):
    ''' Función que recibe un archivo de entrada codificado y la
    rotación deseada y genera un archivo de salida decodificado,
    a partir de la función decodificado_cesar.
    
    Argumentos:
        file(str): Dirección del archivo de entrada codificado.        
        rotate(str): Valor de la rotación deseada para la decodificación.
    
    Retorna:
        file_copy(str):Dirección del archivo de salida decodificado.
        
    '''
    
    try:
        with open(file, 'r') as r_file:
            with open(file_copy, 'w', encoding='utf-8') as w_file:
                for lines in r_file:
                    arch_cod = decodificado_cesar(lines, rotate)
                    w_file.write("".join(arch_cod))
    except FileNotFoundError as error: 
        print("El archivo deseado no se encontró")
 
    return w_file



def principal():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
    En este ejercicio, se ingresa una dirección de archivo a decodificar
    y la rotación deseada y se genera un archivo de salida decodificado.
    Ingrese 1 para ingresar dirección de archivo
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            entrada = input("Ingrese dirección/archivo a decodificar: ")
            salida = entrada + ".decode"
            rotacion = int(input("Ingrese rotación de la decodificación: "))
            resultado = decodificacion(entrada, salida, rotacion)
            print(f'Decodificación exitosa. El archivo decodificado es {salida}')
            sleep(5)
        elif test == 2:
            break



if __name__ == "__main__":
    principal()