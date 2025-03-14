"""
# 2 listas
nombres = ["Dario", "juan", "Pedro", "Maria"]
notas = [50, 80, 70, 95]
# imprimir el nombre seguido de la nota



salida
Dario 50
juan 80
Pedro 70
Maria 95
"""
def lista_clase():
    nombres = ["Dario", "juan", "Pedro", "Maria"]
    notas = [50, 80, 70, 95]

    if(len(nombres) == len(notas)):
        for i in range(len(nombres)):
            print (nombres[i], notas[i])


lista_clase()

def consulta_nombre(cedula):
    personas = {
        11240: "Carlos",
        8382929: "Andrea",
        92233: "Mauricio"
    }

    for i in personas.keys():
        if(i ==cedula):
            return personas[i]

print(consulta_nombre(8382929))


