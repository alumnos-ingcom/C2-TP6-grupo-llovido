################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 12 - Comparación de listas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
import generador_listas as g_lista
from time import sleep


class LongitudDiferente(Exception):
    ''' Error que ocurre cuando las listas tienen
    diferente extensión
    '''
    pass



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def comparacion(lista1,lista2):
    '''
    Funcion que recibe dos listas y compara su contenido sin
    considerar el orden. Si el contenido es el mismo retorna True,
    sino retorna False.    

    Argumentos:
        lista1(list), lista2(list): listas con valores aleatorios.
    
    Retorna:
        ret(bool) = True si el contenido es igual o False si no lo es.
    '''
    
    array_resultados=[]

    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            for j in range(len(lista2)):
                #  print(f"lista1: " + str(lista1[i]))
                #  print(f"lista2: " + str(lista2[j]))
                if lista1[i] == lista2[j]:
                    #resu = "True"
                    array_resultados.append(True)
                    break
                #else:
                    #resu = "False"

    #  if len(lista1) == len(lista2):
    #      for i in range(len(lista1)):
    #          for j in range(len(lista2)):
    #              if lista1[i] == lista2[j]:
    #                  resu = "True"
    #              else:
                    #  resu = "False"
    else:
        raise LongitudDiferente("Las listas tienen diferente extensión")
    
    if len(array_resultados) == len(lista1):
        return True
    else:
        return False

    #return resu
        


def prueba():
    """Toda la interacción con el usuario va acá"""
    
    ext1 = inp.ingreso_entero(f'Ingrese la extensión de la primera lista: ')
    min1 = inp.ingreso_entero(f'Ingrese límite inferior de la primera lista: ')
    max1 = inp.ingreso_entero(f'Ingrese límite superior de la primera lista: ')
    ext2 = inp.ingreso_entero(f'Ingrese la extensión de la segunda lista: ')
    min2 = inp.ingreso_entero(f'Ingrese límite inferior de la segunda lista: ')
    max2 = inp.ingreso_entero(f'Ingrese límite superior de la segunda lista: ')
    lista_uno = g_lista.lista_random(ext1,min1,max1)
    lista_dos = g_lista.lista_random(ext2,min2,max2)
    resultado = comparacion(lista_uno, lista_dos)
    print(f'El resultado de comparar las dos listas es: {resultado}')
    
    

if __name__ == "__main__":
    prueba()

