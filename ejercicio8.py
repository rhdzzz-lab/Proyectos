saldo = 1000

CLAVE_CORRECTA = "5917"
print("="*40)
print("      BIENVENIDO AL CAJERO AUTOMÁTICO")
print("="*40)

clave = input("Por favor, ingresa tu clave de acceso: ")

if clave == CLAVE_CORRECTA:
    print("\n¡Acceso concedido!\n")
    while True:
        print("Menú de opciones:")
        print("1. Consultar saldo")
        print("2. Retirar efectivo")
        print("3. Depositar efectivo")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ")

        match opcion:
            case "1":
                print(f"\nTu saldo actual es: ${saldo:.2f}\n")
            case "2":
                monto = float(input("¿Cuánto deseas retirar?: $"))
                if monto > 0 and monto <= saldo:
                    saldo -= monto
                    print(f"\nRetiro exitoso. Nuevo saldo: ${saldo:.2f}\n")
                else:
                    print("\nMonto inválido o saldo insuficiente.\n")
            case "3":
                monto = float(input("¿Cuánto deseas depositar?: $"))
                if monto > 0:
                    saldo += monto
                    print(f"\nDepósito exitoso. Nuevo saldo: ${saldo:.2f}\n")
                else:
                    print("\nMonto inválido.\n")
            case "4":
                print("\n¡Gracias por usar el cajero automático!\n")
                break
            case _:
                print("\nOpción no válida. Intenta de nuevo.\n")
else:
    print("\nClave incorrecta.\n")

#_________________________________________________________________________________________________________________

print("=" * 47)
print(" BIENVENIDO A ATENCION AL CLIENTE DE RAPIEVIOS")
print("=" * 47)

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, Bienvenid@ a Rapievios")
opciones = input("Ingrese alguna de las siguentes opciones\n1. Raestro de un paquete\n2. Regristo de quejas\n3. Hablar con un agente\n4. Salir del sistema\n")

if opciones.isdigit():
    opciones = int(opciones)
    while opciones <= 1 or opciones >= 4:
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
                  print("Queja no puede estar vacía. Intente nuevamente.")
            case 3:
               print("Usted ha seleccionado hablar con un agente\n Por favor, espere mientras le conectamos con un agente...")
               print("Conectando con un agente...")
               print("¡Conexión exitosa! Un agente estará con usted en breve.")
            case 4:
               print("Saliendo del sistema...\nGracias por usar Rapievios. ¡Vuelva pronto!")
            case _:
               print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")