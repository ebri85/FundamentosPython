# LAb #2

# Funcion calcular factorial

def calcular_factorial(num):
    cont = 0
    resultado=0
    for i in range(1,(num+1)):
        resultado = resultado * i

    print(resultado)

# Funcion calcular si el numero es primo
def es_primo(num):
    for i in range(2,num):
        if num % i == 0:
            return "No es primo"
    return "Es primo"

print(es_primo(27))

# Funcion sumar todos los numeros pares en un rango del 1 al X
def suma_pares(num):
    sum=0
    for i in range(1,num+1):
        if i % 2 ==0:
            sum +=i
    print(f"La suma de los pares es = {sum}")

suma_pares(6)
# Funcion contar el numero de "a" en una palabra

def conta_letras(char,cadena):
    cont = 0
    for i in cadena:
        if char == i:
            cont+=1
    print(f"La letra {char} aparece {cont} veces en el string {cadena}")

conta_letras("a","arrestar")

