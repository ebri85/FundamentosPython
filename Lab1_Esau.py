def datos_personales():
    nombre = input("Digite su nombre ")
    edad = int(input("Digite su Edad "))
    altura = float(input("Digite su altura en metros "))
    print(nombre,edad,altura)
    cantidad_letras = len(nombre)
    edad_es_par = ("True", 'False')[cantidad_letras % 2==0]
    altura_cms= altura *100

    print(nombre,"su nombre contiene la siguiente cantidad de letras: ", cantidad_letras)
    print("Su edad es par? ", edad_es_par)
    print("La altura digitada en centimeros es: ", altura_cms)


datos_personales()

def divisible():
    num1 = int(input("Digite un numero "))
    num2 = int(input("Digite otro numero "))
    es_divisible = ("No","Si")[num1 % num2 == 0 ]
    print("El numero ",num1,es_divisible, "es divisible entre ", num2)

divisible()

def sumar():
    num1 = int(input("Digite un numero "))
    num2 = int(input("Digite otro numero "))
    suma = num1 + num2
    print("El resultado de la suma de los numeros es ", suma)

sumar()
