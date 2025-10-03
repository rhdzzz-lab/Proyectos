"""
estudiantes = ["Daniel", "Feramay", "Joshua"]

notas = [90, 70, 50]

notas[0] = 86

#print(f"El estudiante {estudiantes[2]} obtuvo una nota de: {notas[0]}")

opciones = input("A cual de los estudiantes desea editar {estudiantes}")

if opciones.isdigit():
    opciones = int(opciones)
    if opciones < len(estudiantes)-1:
        estudiantes[opciones] = input("Ingrese el nuevo valor para el estudiante {estudiantes [opciones]} ")
    else:
        print()
"""


print("*" * 23)
print(" BIENVENIDO BUEN SABOR")
print("*" * 23)

alimentos = ["Hamburgesa", "Pizza", "Ensalada", "Sopa", "Tacos"]
precios = [35, 20, 65, 50, 25]

print(f"Menú de alimentos:\n0.{alimentos[0]} - ${precios[0]:.2f}\n1.{alimentos[1]} - ${precios[1]:.2f}\n2.{alimentos[2]} - ${precios[2]:.2f}\n3.{alimentos[3]} - ${precios[3]:.2f}\n4.{alimentos[4]} - ${precios[4]:.2f}")
opcion = input("Seleccione el número del alimento que desea editar (0-4): ")
if opcion.isdigit():
    match int(opcion):
        case 0:
            print(f"Usted ha seleccionado {alimentos[0]} que cuesta ${precios[0]:.2f}")
            pago = float(input("Ingrese el monto que desea pagar: $"))
            if pago >= precios[0]:
                cambio = pago - precios[0]
                print(f"Pago exitoso. Su cambio es: ${cambio:.2f}")
            else:
                print("Monto insuficiente. Por favor, intente nuevamente.")
        case 1:
            print(f"Usted ha seleccionado {alimentos[1]} que cuesta ${precios[1]:.2f}")
            pago = float(input("Ingrese el monto que desea pagar: $"))
            if pago >= precios[1]:
                cambio = pago - precios[1]
                print(f"Pago exitoso. Su cambio es: ${cambio:.2f}")
            else:
                print("Monto insuficiente. Por favor, intente nuevamente.")
        case 2:
            print(f"Usted ha seleccionado {alimentos[2]} que cuesta ${precios[2]:.2f}")
            pago = float(input("Ingrese el monto que desea pagar: $"))
            if pago >= precios[2]:
                cambio = pago - precios[2]
                print(f"Pago exitoso. Su cambio es: ${cambio:.2f}")
            else:
                print("Monto insuficiente. Por favor, intente nuevamente.")
        case 3:
            print(f"Usted ha seleccionado {alimentos[3]} que cuesta ${precios[3]:.2f}")
            pago = float(input("Ingrese el monto que desea pagar: $"))
            if pago >= precios[3]:
                cambio = pago - precios[3]
                print(f"Pago exitoso. Su cambio es: ${cambio:.2f}")
            else:
                print("Monto insuficiente. Por favor, intente nuevamente.")
        case 4:
            print(f"Usted ha seleccionado {alimentos[4]} que cuesta ${precios[4]:.2f}")
            pago = float(input("Ingrese el monto que desea pagar: $"))
            if pago >= precios[4]:
                cambio = pago - precios[4]
                print(f"Pago exitoso. Su cambio es: ${cambio:.2f}")
            else:
                print("Monto insuficiente. Por favor, intente nuevamente.")
        case _:
            print("Opción no válida. Por favor, seleccione un número entre 0 y 4.")


"""
provincias = ["Alajuela", "San José", "Heredia"]

provincias = input("Ingrese una provincia a la lista: ")

provincias.append(provincias)

print(f"Lista de provincias actualizada:\n {provincias}")

provincias.extend(["Cartago", "Guanacaste", "Puntarenas", "Limón"])

print(f"Lista de provincias extendida:\n {provincias}")

provincias.insert(1, "Puntarenas")

print(f"Provincia insertada:\n {provincias}")

provincias.remove("Puntarenas")

print(f"Provincia eliminada:\n {provincias}")

provincias.pop()

print(f"Provincia eliminada por índice:\n {provincias}")

provincias.sort(revers = True)

print(f"Lista de provincias ordenada de manera desendente:\n {provincias}")
"""