################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from random import randint

def lista_random(cantidad=10, numero_minimo=0, numero_maximo=100):
    """
    Esta función genera una lista de `cantidad` 
    con valores entre `número_minimo` y `número_maximo`
    Con valores por defecto sensibles para su uso rápido
        (10 elementos, entre 0 y 100)
    """
    milista = list()
    for i in range(cantidad):
        milista.append(randint(numero_minimo, numero_maximo))
    return milista

def prueba():
    print("Generando una lista aleatoria de 10 elementos entre 0 y 100")
    aleatoria = lista_random()
    print(f"La lista contiene {aleatoria}")

if __name__ == "__main__":
    prueba()
