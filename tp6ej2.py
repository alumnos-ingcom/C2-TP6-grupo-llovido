################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 2 - Anagrama II
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp6ej1 import anagrama
from time import sleep
from tp5ej12 import LongitudDiferente



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def separacion(lista):
    '''
    Esta función recibe una lista con las dos cadenas a comparar y
    retorna dos listas con las cadenas separadas.
    
    Argumento:
        lista(list): Lista con los términos de las dos cadenas a
        comparar.
    
    Retorna:
        listados(list):Lista con términos de la cadena número uno.
        listatres(list):Lista con términos de la cadena número dos.
    '''
    
    flag = 0
    listados = []
    listatres = []
    linea = lista.split()
    for i in linea:
        if i != '–':
            if flag == 1:
                listatres.append(i)
            else:
                listados.append(i)
        else:
            flag = 1
            
    devolucion1 =  "".join(listados)
    devolucion2 =  "".join(listatres)
    print(' ')
    print(devolucion1)
    print(devolucion2)

    return "".join(listados), "".join(listatres) 
                
                
                
def anagrama_archivo(file):
    '''
    Esta función recibe la dirección de un archivo con un listado de
    posibles anagramas y analiza cada línea.
    
    Esta función muestra los resultados de la evaluación por consola.
    
    Ejemplo:    
        Alegan – Ángela
        True
        
        La contravino – No la vi entrar
        False
    
    Argumento:
        file(str): Dirección del archivo a evaluar.              
    '''
    
    with open(file, 'r', encoding='utf-8') as file_object:
        data = file_object.readlines()     
    for j in data:
        frase1,frase2 = separacion(j)
        try:
            print(anagrama(frase1,frase2))
        except LongitudDiferente:
            print(False)
            
        

def principal(): 
    """Toda la interacción con el usuario va acá"""

    direccion = input("Ingrese dirección/archivo: ")
    anagrama_archivo(direccion)



if __name__ == "__main__":
    principal()