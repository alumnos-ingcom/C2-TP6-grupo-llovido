################
# Martín René - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp5ej12 import comparacion



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
        l = transformacion(letra)
        print(l)
        resultado.append(l)
    return "".join(resultado)



def principal():
    """Toda la interacción con el usuario va acá"""
    palabra1 = 'El huevo de chocolate'
    nor_palabra1 = normalizacion(palabra1)
    palabra2 = 'hecho de vate locuelo'
    nor_palabra2 = normalizacion(palabra2)
    print(f"{palabra1}: {nor_palabra1}")
    print(f"{palabra2}: {nor_palabra2}")
    print(f"{comparacion(nor_palabra1, nor_palabra2)}")


if __name__ == "__main__":
    principal()

