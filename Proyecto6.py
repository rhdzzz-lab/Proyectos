print("="*40)
print("SISTEMA DE RESERVAS - CINE PYTHON")
print("="*40)

# Inicializar la sala: 5 filas x 5 asientos, todos "Libre"
sala = [["Libre" for _ in range(5)] for _ in range(5)]

# Diccionario para registrar clientes: {nombre: (fila, asiento)}
clientes = {}

while True:
    print("\nMenú:")
    print("1. Consultar sala")
    print("2. Reservar asiento")
    print("3. Ver lista de clientes")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("\nEstado actual de la sala (F=Fila, A=Asiento):")
        for i in range(5):
            fila_estado = ""
            for j in range(5):
                fila_estado += f"[{sala[i][j]:^7}]"
            print(f"Fila {i+1}: {fila_estado}")
    elif opcion == "2":
        nombre = input("Nombre del cliente: ").strip().title()
        try:
            fila = int(input("Ingrese la fila (1-5): ")) - 1
            asiento = int(input("Ingrese el número de asiento (1-5): ")) - 1
            if 0 <= fila < 5 and 0 <= asiento < 5:
                if sala[fila][asiento] == "Libre":
                    sala[fila][asiento] = "Ocupado"
                    clientes[nombre] = (fila+1, asiento+1)  # Guardar como tupla (fila, asiento)
                    print(f"Asiento reservado exitosamente para {nombre} en Fila {fila+1}, Asiento {asiento+1}.")
                else:
                    print("Ese asiento ya está ocupado. Elija otro.")
            else:
                print("Fila o asiento fuera de rango.")
        except ValueError:
            print("Por favor, ingrese números válidos para fila y asiento.")
    elif opcion == "3":
        if clientes:
            print("\nLista de clientes y sus asientos reservados:")
            for nombre, ubicacion in clientes.items():
                print(f"{nombre}: Fila {ubicacion[0]}, Asiento {ubicacion[1]}")
        else:
            print("No hay reservas registradas.")
    elif opcion == "4":
        print("¡Gracias por usar el sistema de reservas del cine!")
        break
    else:
        print("Opción no válida.")