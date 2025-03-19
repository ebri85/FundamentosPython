""" Menu Dinamico"""

with open("canciones.txt","w") as canciones:
    canciones.write("")


with open("juegos.txt","w") as juegos:
    juegos.write("")
    

with open("series.txt","w") as series_tv:
    series_tv.write("")

def menu_principal():
    resultado = "=====Hola Bienvenido==== \n"
    resultado +="Desea agregar un Item ? \n"
    resultado +="1. Lista de Series\n"
    resultado +="2. Lista de Canciones \n"
    resultado +="3. Lista de Juegos \n"
    resultado +="4. Salir \n"
   
    print(resultado)
    
def agregar(op,nombre):
    if op == '1':
        with open("series.txt","a") as series_tv:
            series_tv.write(nombre)
    if op == '2':
        with open("canciones.txt","a") as canciones:
            canciones.write(nombre)
    if op == '3':
        with open("series.txt","a") as juegos:
            juegos.write(nombre)
            

def ejecutar():    
    
    while True:
        menu_principal()
        opcion = input("Seleccione una opcion")
        
        if opcion == '1':
            agregar(opcion,input("Escriba el nombre de la serie que desea agregar"))
        
        elif opcion == '2':
            agregar(opcion,input("Escriba el nombre de la cancion que desea agregar"))
        
        elif opcion == '3':
            agregar(opcion,input("Escriba el nombre del juego que desea agregar"))
            
        elif opcion == '4':
            print("Adios!! \n Termina Programa")
            
            break
        
ejecutar()