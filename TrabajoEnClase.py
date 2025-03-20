lista_productos=[]


def menu_principal():
    resultado = "=====Hola Bienvenido==== \n"
    resultado += "Desea agregar un Item ? \n"
    resultado += "1. Agregar Producto\n"
    resultado += "2. Salir \n"

    print(resultado)

def ejecutar():
    while True:
        menu_principal()
        opcion = input("Seleccione una opcion \n")

        if opcion=="1":
            lista_productos.append(input("Ingrese el producto a la lista\n"))

        elif opcion=="2":
            #print(lista_productos)
            for i in lista_productos:
                with open("productos.txt","a") as productos:
                    productos.write(f"{i}\n")

            print("Adios!")
            break
        else:
            print("Opcion digitada no se encuentra en el menu")

ejecutar()