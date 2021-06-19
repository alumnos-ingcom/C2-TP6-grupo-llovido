################
# Biagini Agostina  - @AgostinaB
# Evaraldo Adrian   - @chim20air
# Ejercicio 1 - Anagramas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as inp
from tp5ej13 import search
from tp5ej12 import comparacion
from time import sleep



def limpiar_consola():
    '''Funcion para limpiar la salida de la consola'''
    print('\033[2J')



def hace_etiqueta(contenido, etiqueta, source=None):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el
    segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará
    <h1>Hola</h1>
    '''
    #lista de etiquetas que tienen un enter al final de cada tag para mayor legibilidad
    lista_etiquetas_enter = ['html', 'head', 'body']
    #lista de etiquetas que solo tienen enter al final
    lista_etiquetas = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title', 'ul', 
                       'ol', 'li']
    lista_src = ['img']
    lista_href = ['a']
    if source == None:
        if search(lista_etiquetas_enter, etiqueta):
            lista_buffer = ['<', etiqueta, '> \n', contenido, '</', etiqueta, '>\n']
        elif search(lista_etiquetas, etiqueta):
            lista_buffer = ['<', etiqueta, '> ', contenido, ' </', etiqueta, '>\n']
        else:
            lista_buffer = ['<', etiqueta, '> ', contenido, ' </', etiqueta, '>']
    else:
       if search(lista_src, etiqueta):
           lista_buffer = ['<', etiqueta, ' src=', source,  '> ', contenido,
                          ' </', etiqueta, '>']
       elif search(lista_href, etiqueta):
           lista_buffer = ['<', etiqueta, ' href=', source,  '> ', contenido,
                            ' </', etiqueta, '>']
    return "".join(lista_buffer)

def hace_comenta(contenido):
    '''
    Retorna el contenido envuelto en las marcas de comentario HTML
    <!--  -->
    (separen las marcas del contenido con un espacio)
    '''
    lista_buffer = ['<!-- ', contenido, ' -->\n']
    return "".join(lista_buffer)



def principal():
    """Toda la interacción con el usuario va acá"""
    while True:
        limpiar_consola()
        print("""
En este ejercicio, se ingresan dos cadenas de
texto y la función retorna si son anagramas.
    Ingrese 1 para ingresar etiqueta
    Ingrese 2 para ingresar comentario
    Ingrese 3 para ingresar imagen
    Ingrese 4 para ingresar link
    Ingrese 5 para ingresar una imagen con link
    Ingrese 6 para generar una pagina web basica
    Ingrese 7 para terminar la prueba""")

        test = inp.ingreso_entero_restringido("ingrese opción", 1, 7)
        if test == 1:
            label = input("Ingrese etiqueta: ")
            content = input(f"Ingrese contenido de {label}: ")
            resultado = hace_etiqueta(content, label)
            print(f'Resultado: {resultado}')
            sleep(5)
        elif test == 2:
            content = input("Ingrese contenido del comentario: ")
            resultado = hace_comenta(content)
            print(f'Resultado: {resultado}')
            sleep(5)
        elif test == 3:
            content = input("Ingrese texto alterantivo de la imagen: ")
            src = input("Ingrese la dirección de la imagen: ")
            resultado = hace_etiqueta(content, 'img', source=src)
            print(f'Resultado: {resultado}')
            sleep(5)
        elif test == 4:
            content = input("Ingrese el texto del enlace: ")
            link = input("Ingrese el link del enlace: ")
            resultado = hace_etiqueta(content, 'a', source=link)
            print(f'Resultado: {resultado}')
            sleep(5)
        elif test == 5:
            src = input("Ingrese la dirección de la imagen: ")
            content = input("Ingrese el texto alternativo de la imagen: ")
            link = input("Ingrese el link: ")
            buffer = hace_etiqueta(content, 'img', source=src)
            resultado = hace_etiqueta(buffer, 'a', source=link)
            print(f"Resultado: {resultado}")
            sleep(5)
        elif test == 6:
            titulo = input("Ingrese el título de la página: ")
            Encabezado = input("Ingrese el encabezado de la pagina: ")
            testo = input("Ingrese el texto de la misma: ")
            name = input("Ingrese el nombre del archivo saliente sin '.html': ")
            cuerpo_a = hace_etiqueta(Encabezado, 'h1')
            cuerpo_b = hace_etiqueta(testo, 'p')
            cuerpo = hace_etiqueta(cuerpo_a + cuerpo_b, 'body')
            header = hace_etiqueta(titulo, 'title')
            cabeza = hace_etiqueta(header, 'head')
            web = hace_etiqueta(cabeza + cuerpo, 'html')
            print(f'La pagina resultante:\n{web}')
            with open(name + '.html', 'w') as out:
                out.write(web)
            sleep(10)
        elif test == 7:
            break



if __name__ == "__main__":
    principal()

