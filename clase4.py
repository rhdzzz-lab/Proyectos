# Ejemplo and
edad1 = input("Ingrese la edad del cliente 1 para ver la película de terror: ")
edad2 = input("Ingrese la edad del cliente 2 para ver la película de terror: ")

edad1 = int(edad1)
edad2 = int(edad2)

mayoriaEdad = edad1 >= 18 and edad2 >= 18
print(f"Ambos clientes cumplen pueden entrar a ver la pelucila de terror? {mayoriaEdad}")

# Ejemplo or
edad1 = input("Ingrese la edad del cliente 1 para ver la película de terror: ")
edad2 = input("Ingrese la edad del cliente 2 para ver la película de terror: ")

edad1 = int(edad1)
edad2 = int(edad2)

mayoriaEdad = edad1 >= 18 or edad2 >= 18
print(f"Ambos clientes cumplen pueden entrar a ver la pelucila de terror? {mayoriaEdad}")

# Ejemplo 
edad1 = input("Ingrese la edad del cliente 1 para ver la película de terror: ")
edad2 = input("Ingrese la edad del cliente 2 para ver la película de terror: ")

edad1 = int(edad1)
edad2 = int(edad2)

mayoriaEdad = edad1 >= 18 or edad2 >= 18 and edad1 >=12 and edad2 >= 12
print(f"Ambos clientes cumplen pueden entrar a ver la pelucila de terror? {mayoriaEdad}")

#Ejercicio 6
ana = 20
juan = 20
pedro = 18

anaMayorjuan = ana > juan

juanIgualPedro = juan == pedro

pedroIgualMenorAna = pedro <= ana

todosIgual = (ana == juan) and (juan == pedro)

mayor18 = (ana > 18 ) or (juan > 18) or (pedro > 18)

print()

edad1 = input("Ingrese su edad")
if(edad1.isdigit()):
    print("Muy bien la edad ingresada es un numero")
    edad1 = int(edad1)
    if(edad1 >= 18):
        print("El cliente puede ingresar a la sala de cine")
    else:
        print("El cliente no puede ingresar a la sala de cine porque no tiene la mayoria de edad")
  
else:
    print("La edad ingresada no es un numero \nIntentelo de nuevo...")
    
    
opciones = input("Ingrese una opcion\n1.Ingresar Nombre\n2.Salir del sistema")
nombre = ""
if(opciones.isdigit()):
    opciones = int(opciones)

    if(opciones == 1):
        nombre = input("Ingrese su nombre")
    
    elif(opciones == 2):
        print("Saliendo del sistema\nVuelva pronto...")
        
    else:
        print("Opcion Invalida.\n Intente de nuevo")

        
else:
    print("No ingreso un numero")
