#match-case(switch)
opciones = input("Ingrese una opción\n1, Ingrese Nombre\n2.Salir del sistema")
if(opciones.isdigit()):
    opciones = int(opciones)
    match opciones:
        case 1: 
            nombre = input("Ingrese su nombre: ")

        case 2:
            print("Saliendo del sistema...\nVuelva pronto")
else:
    print("Opcion invalida\nDigite un numero valido")

opciones = input("Te llamas Jvaier, Dylan o Victor?")
match opciones:
    case "Javier":
        print("Mucho gusto Javier")
    case "Dylan":
        print("Mucho gusto Dylan")
    case "Victor":
        print("Mucho gusto Victor")
    case _:
        print("No es ningun usuario conocido\nNo puede ingresar al sistema")


numero = 5
numero += 20
print(f"El numero es {numero}")

nomnbre = "Dylan"
nombre+= "Profesor de Python"
print(f"El nombre es {nombre}")

numero = 5
numero -= 2
print(f"El numero es {numero}")

