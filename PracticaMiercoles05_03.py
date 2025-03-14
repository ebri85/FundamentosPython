""""
def suma(num1, num2):
    resultado = num1 + num2
    print("La suma de esos numeros es: ", resultado)


def resta(num1, num2):
    resultado = num1 - num2
    print("La resta de esos numeros es: ", resultado)


def division(num1, num2):
    resultado = num1 / num2
    print("La division de esos numeros es: ", resultado)


def multiplicacion(num1, num2):
    resultado = num1 * num2
    print("La division de esos numeros es: ", resultado)


def calculos(num1,num2):
    print("##### Tabla de Resultados \n")
    suma(num1,num2)
    resta(num1, num2)
    multiplicacion(num1, num2)
    division(num1, num2)


calculos(4,2)


def contar_mill():
    num=1
    while num <=10000:
        print(num)
        num = num + 1


def contar_for():
    for num in range(1,10001):
        print(num)
contar_for()


def encontrar_caracter(char,cadena):
    for i in cadena:
        print(i)
        if(i== char):
            print(f"Encontre el caracter {char}")
            break
    print("Final de la revision")

encontrar_caracter("a","sdfsadfsdfa")
"""