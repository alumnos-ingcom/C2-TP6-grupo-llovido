################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 8 - Cifrado del Cesar
# UNRN Andina - Introducción a la Ingenieria en Computación
################
'''
El cifrado César o cifrado de rotación usa una encriptación de sustitución
simple. Esto significa que cada caracter se sustituye por otro caracter
de acuerdo con un sistema especifico. 

La codificación debe ser tal que la palabra codificada contenga unicamente
caracteres del tipo A-Z a-z y 0 a 9, de manera que al codificar las ultimas
letras del abecedario se vuelva a las primeras letras.

**Por ejemplo**, el método conocido y muy utilizado ROT13 rota el alfabeto
con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.
'''


import tp4ej1 as inp
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def rotacion(letra, rotate, minimo, maximo):
    if letra >= minimo and letra <= maximo:
        letra += rotate
        if letra > maximo:
            if maximo == ord('9'): #si es digito, tengo que volver menos
                letra -= 10
            else:                  #si es letra, vuelvo mas
                letra -= 26
        if letra < minimo:
            if minimo == ord('0'):
                letra += 10
            else:
                letra += 26
    return letra



def codificado_cesar(texto, rotate):
    '''
    Funcion que implementa el cifrado cesar a una cadena de caracteres.

    Argumentos:
        texto(str):     cadena de caracteres a ser codificada
        rotate(int):    cantidad de posiciones a rotar el caracter

    Retorna:
        ret(str):       cadena de caracteres codificada segun el valor
                        de rotate
    '''
    modificado = []
    for i in range(len(texto)):
        n = ord(texto[i])
        
        if n >= ord('0') and n <= ord('9'):
            #digitos
            valor = rotacion(n, rotate, ord('0'), ord('9'))

        elif n >= ord('A') and n <= ord('Z'):
            #mayusculas
            valor = rotacion(n, rotate, ord('A'), ord('Z'))

        elif n >= ord('a') and n <= ord('z'):
            #minusculas
            valor = rotacion(n, rotate, ord('a'), ord('z'))
        
        modificado.append(str(chr(valor)))

    return "".join(modificado)



def decodificado_cesar(text, rotate):
    '''
    Funcion que implementa el decifrado cesar a una cadena de caracteres.

    Argumentos:
        texto(str):     cadena de caracteres a ser codificada
        rotate(int):    cantidad de posiciones a rotar el caracter

    Retorna:
        ret(str):       cadena de caracteres codificada segun el valor
                        de rotate
    '''
    return codificado_cesar(text, (-1) * rotate)



def prueba():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresa un texto y una 
cantidad de numeros a rotar para el codificado
y decodificado de cesar
    Ingrese 1 para codificar texto
    Ingrese 2 para decodificar texto
    Ingrese 3 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 3)
        if test == 1:
            rotacion = inp.ingreso_entero("Ingrese el valor de la rotacion")
            testo = input("ingrese el texto a codificar >>> ")
            resultado = codificado_cesar(testo, rotacion)
            print(f'''La codificacion del texto {testo} con rotacion {rotacion} es:
                    {resultado}''')
            sleep(10)
        elif test == 2:
            rotacion = inp.ingreso_entero("Ingrese el valor de la rotacion")
            testo = input("ingrese el texto a decodificar >>> ")
            resultado = decodificado_cesar(testo, rotacion)
            print(f'''La decodificacion del texto {testo} con rotacion {rotacion} es:
                    {resultado}''')
            sleep(3)
        elif test == 3:
            break    



if __name__ == "__main__":
    prueba()

