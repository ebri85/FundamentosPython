"""
- Hacer una funcion que busque el numero mas pequeno en una lista, no se puede usar min ni ninguna funcion de Python

- Funcion, de una lista de palabras, generar una lista de cantidad de palabras respectivamente
"""
def num_menor():
    numeros = [1,2,3,5,3,6,7,5,6,13,41,21,54,21]
    min = numeros[0]
    l = 0
    for i in range(1,len(numeros)):
        if i < min:
            min = numeros[i]

    return min

print(num_menor())
"""
- Funcion para obtener la posicion del primer numero no repetido de una lista
"""

def num_repetido():
    numeros = [1,2,3,5,3,6,7,5,6,13,41,21,54,21]
    repetido = numeros[0]
    posicion =0
    for i in range(1,len(numeros)):
        if i == repetido:
            posicion

    return repetido

print(num_menor())