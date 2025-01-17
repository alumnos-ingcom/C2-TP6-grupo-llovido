################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 4 - Codificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp5ej8 import codificado_cesar
from time import sleep


class FileNotFoundError(Exception):
    ''' Error que genera cuando no se encuentra el archivo.'''
    pass



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def codificacion(file, file_copy, rotate):
    ''' Función que recibe un archivo de entrada y la rotación deseada
    y genera un archivo de salida codificado, a partir de la función
    codificado_cesar
    
    Argumentos:
        file(str): Dirección del archivo de entrada.        
        rotate(str): Valor de la rotación deseada para la codificación.
    
    Retorna:
        file_copy(str):Dirección del archivo de salida codificado.
        
    '''
    
    try:
        with open(file, 'r') as r_file:
            with open(file_copy, 'w', encoding='utf-8') as w_file:
                for lines in r_file:
                    arch_cod = codificado_cesar(lines, rotate)
                    w_file.write("".join(arch_cod))
    except FileNotFoundError as error: 
        print("El archivo deseado no se encontró")
 
    return w_file



def principal():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
    En este ejercicio, se ingresa una dirección de archivo a codificar
    y la rotación deseada y se genera un archivo de salida codificado.
    Ingrese 1 para ingresar dirección de archivo
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            entrada = input("Ingrese dirección/archivo a codificar: ")
            salida = entrada + ".cesar"
            rotacion = int(input("Ingrese rotación de la codificación: "))
            resultado = codificacion(entrada, salida, rotacion)
            print(f'Codificación exitosa. El archivo codificado es {salida}')
            sleep(5)
        elif test == 2:
            break



if __name__ == "__main__":
    principal()