"""
- Hacer una funcion que busque el numero mas pequeno en una lista, no se puede usar min ni ninguna funcion de Python

"""
def num_menor():
    numeros = [4,2,3,5,3,6,7,5,6,13,41,1,21,54,21]
    min = numeros[0]
    l = 0
    for i in numeros:
        if i < min:
            min = i

    return min

print("El numero menor de la lista es ",num_menor())
"""
- Funcion para obtener la posicion del primer numero no repetido de una lista
"""

def num_no_repetido():
    numeros = [1,2,3,2,1,5,3,6,7,5,6,13,41,21,54,21]
    for i in range(len(numeros)):
        cont =0
        for j in range(len(numeros)):
            if numeros[i]== numeros[j]:
                cont += 1
        if cont == 1:
            return i
 
 
print("La posicion del primer numero no repetido es ",num_no_repetido())


"""- Funcion, de una lista de palabras, generar una lista de cantidad de palabras respectivamente
"""
