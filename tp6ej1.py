################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 1 - Anagramas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp5ej12 import comparacion
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def transformacion(letra_entrada):
    '''
    Funcion que recibe una letra en cualquier formato y la transforma
    a mayuscula sin acentuar

    Argumentos:
        letra_entrada(str): letra a modificar

    Retorna:
        letra(str): letra modificada
    '''
    letra = ord(letra_entrada)
    if letra >= ord('a') and letra <= ord('z'):
        letra -= 32
    elif letra == ord('á') or letra == ord('Á'):
        letra = ord('A')
    elif letra == ord('é') or letra == ord('É'):
        letra = ord('E')
    elif letra == ord('í') or letra == ord('Í'):
        letra = ord('I')
    elif letra == ord('ó') or letra == ord('Ó'):
        letra = ord('O')
    elif letra == ord('ú') or letra == ord('Ú'):
        letra = ord('U')
    elif letra == ord('ö') or letra == ord('Ö'):
        letra = ord('O')
    elif letra == ord('ü'):
        letra = ord('U')
    elif letra == ord('ñ') or letra == ord('Ñ'):
        letra = ord('N')
    return chr(letra)



def normalizacion(string):
    '''
    Funcion que recibe una cadena de texto y convierte el formato a
    mayusculas, ignorando espacios, diferencia entre mayusculas y
    minusculas y acentos.

    Argumentos:
        string(str): Cadena de texto a normalizar

    Retorna:
        resultado(str): Cadena de texto normalizada
    '''
    resultado = []
    for letra in string:
        if ord(letra) != 32 and ord(letra) != ord(","):
            l = transformacion(letra)
            resultado.append(l)
    return "".join(resultado)



def anagrama(palabra1,palabra2):
    nor_palabra1 = normalizacion(palabra1)
    nor_palabra2 = normalizacion(palabra2)
    return comparacion(nor_palabra1,nor_palabra2)



def principal():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresan dos cadenas de
texto y la función retorna si son anagramas.
    Ingrese 1 para ingresar frases
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            palabra1 = input("Ingrese primera frase: ")
            palabra2 = input("Ingrese segunda frase: ")
            resultado = anagrama(palabra1, palabra2)
            print(f'La evaluación resultó: {resultado}')
            sleep(5)
        elif test == 2:
            break

if __name__ == "__main__":
    principal()

