################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 13 - Busqueda de palabras
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



class Error404PalabraNoEncontrada(Exception):
    '''Error que indica que la palabra no fue encontrada'''
    pass


def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def separacion(string, char=''):
    '''
    Función customizable para separar una cadena de caracteres
    en palabras.

    Argumentos:
        string(str):    cadena de caracteres a separar
        char(str):      caracter para indicar la separacion
                        por defecto es un espacio
    Retorna:
        ret(list):      lista con las palabras separadas de
                        la entrada
    '''
    ret = []
    word = []
    for letra in range(len(string)):
        if ord(string[letra]) != ord(char):
            word.append(s[letra])
            if letra == len(string) - 1:
                ret.append("".join(word))
                word.clear()
        else:
            ret.append("".join(word))
            word.clear()
    return ret



def search(lista, word):
    '''
    Función que busca una palabra dentro de un string.

    Argumentos:
        lista(list):    lista de palabras
        word(str):      palabra a buscar

    Retorna:
        ret(bool):      True si la palabra fue hallada
                        False en caso contrario
    '''
    for palabra in lista:
        if palabra == word:
            ret = True
            break
        else:
            ret = False

    return ret

def busqueda_palabras(string, word):
    '''
    Funcion que dado un string, busca la palabra ingresada y devuelve
    la ubicacion en el texto o levanta una excepcion en caso de que 
    no exista tal palabra

    Argumentos:
        string(str):    cadena de caracteres en la que se desea buscar
        word(str):      palabra a buscar en string

    Retorna:
        ret(list):      lista de posiciones en las que se encuentra
                        la palabra objetivo
    '''
    entrada = separacion(string)
            
    if not search(entrada, word):
        raise Error404PalabraNoEncontrada(f"la palabra {word} no se encuentra en la entrada")

    ret = []
    for i in range(len(entrada)):
        if entrada[i] == word:
            ret.append(i)

    return ret



def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se debe ingresar un texto y una
palabra a buscar. La funcion debe levantar una excepcion
en el caso de que la palabra no exista dentro del texto,
en caso contrario, retorna una lista con las posiciones
de los aciertos
    Ingrese 1 para ingresar texto y palabra a buscar
    Ingrese 2 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
        if test == 1:
            texto = input("Ingrese texto: ")
            palabra = input("Ingrese palabra a buscar: ")
            resultado = busqueda_palabras(texto, palabra)
            print(f'La inversión queda: {resultado}')            
            sleep(10)
        elif test == 2:
            break       


if __name__ == "__main__":
    prueba()

