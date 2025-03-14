def saludar():
    nombre= "Esau"
    edad = 39
    print('Hola',nombre, 'tu edad es', edad)


#saludar()

def check_condicional():
    condicion1= True
    condicion2= False
    condicion3=20>10
    condicion4= 5 == 9
    print(condicion1)
    print(condicion2)
    print(condicion3)
    print(condicion4)
    condicional5= condicion1 or condicion4
    print ("----", condicional5)
    condicional6 = condicion1 and condicion4
    print("----", condicional6)

check_condicional()

