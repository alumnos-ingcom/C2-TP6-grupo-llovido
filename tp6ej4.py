################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 4 - Codificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp5ej8 import codificado_cesar
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def codificado(file, rotate):
#    with open(file, 'r', encoding='utf-8') as r_file:
#         r_file_cont = r_file.readlines()
#         print(r_file_cont)
    r_file_cont = ['6789', 'abCD']
    for i in r_file_cont:
        print(i)
        for j in range(len(i)):
            print(i[j])
#             print(type(i[j]))
#             if i[j] != '\n':
#                 evaluacion = codificado_cesar(i[j], rotate) 
#                 print(evaluacion)
    




def principal():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresa una dirección de archivo a codificar
y la rotación deseada y se genera un archivo de salida codificado.
#     Ingrese 1 para ingresar dirección de archivo
#     Ingrese 2 para terminar la prueba""")

#        test = inp.ingreso_entero_restringido("ingrese opción", 1, 2)
#        if test == 1:
        entrada_dos = 'entrada_dos.txt' #input("Ingrese dirección/archivo a codificar: ")
        rotacion = 1 #int(input("Ingrese rotación de la codificación: "))
        codificado(entrada_dos, rotacion)
        
#        print(resu)
#             salida_dos = codificador(entrada_dos, rotacion)
#             print(f'El archivo {entrada_dos} fue codificado en {salida_dos}')
#        sleep(5)
#        elif test == 2:
#            break


if __name__ == "__main__":
    principal()