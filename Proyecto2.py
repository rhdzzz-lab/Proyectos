print("=" * 47)
print(" BIENVENIDO A ATENCION AL CLIENTE DE RAPIEVIOS")
print("=" * 47)

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, Bienvenid@ a Rapievios")

while True:
    opciones = input("\nIngrese alguna de las siguientes opciones\n1. Rastreo de un paquete\n2. Registro de quejas" +
                     "\n3. Hablar con un agente\n4. Salir del sistema\n")
    if opciones.isdigit():
        opciones = int(opciones)
        match opciones:
            case 1:
                print("Usted ha seleccionado el rastreo de un paquete")
                numero_paquete = input("Ingrese el número de su paquete (máx. 8 dígitos): ")
                if numero_paquete.isdigit() and len(numero_paquete) <= 8:
                    print(f"Rastreando el paquete {numero_paquete}...\nEstado: En camino a su destino.")
                else:
                    print("Número de paquete inválido. Debe ser numérico y de máximo 8 dígitos. Intente nuevamente.")
            case 2:
                print("Usted ha seleccionado el registro de quejas")
                queja = input("Ingrese su queja: ")
                if queja:
                    print(f"Queja registrada: {queja}")
                else:
                    print("La queja no puede estar vacía. Intente nuevamente.")
            case 3:
                print("Usted ha seleccionado hablar con un agente\nPor favor, espere mientras le conectamos con un agente...")
                print("Conectando con un agente...")
                print("¡Conexión exitosa! Un agente estará con usted en breve.")
            case 4:
                print("Saliendo del sistema...\nGracias por usar Rapievios. ¡Vuelva pronto!")
                break
            case _:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")
    else:
        print("Por favor, ingrese solo números del 1 al 4.")