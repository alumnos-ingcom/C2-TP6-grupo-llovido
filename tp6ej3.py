################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 3 - Copiadora
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')
                
            
              
def copiar_archivo(file, file_copy):
    '''
    Esta función recibe la dirección de un archivo de entrada y copia
    el contenido en otro archivo de salida.
    
    Argumento:
        file(str): Dirección del archivo de entrada a copiar.
    
    Retorna:
        file(str): Dirección de archivo de salida copiado.
    '''
    
    with open(file, 'r', encoding='utf-8') as r_file:
        with open(file_copy, 'w', encoding='utf-8') as w_file:
#            data = file_object.readlines()     
            for line in r_file:
                w_file.write(line)
    return(w_file)


            
        

def principal(): 
    """Toda la interacción con el usuario va acá"""

    entrada = input("Ingrese dirección/archivo a copiar: ")
    salida = input("Ingrese dirección/archivo dónde guardar copia: ")
    copiar_archivo(entrada, salida)
    print(f'El archivo {entrada} fue copiado en {salida}')



if __name__ == "__main__":
    principal()