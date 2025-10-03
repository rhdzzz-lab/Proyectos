print("="*40)
print("SISTEMA SECRETO DE PRÉSTAMO DE LIBROS")
print("="*40)

# 1. Solicitar contraseña
CONTRASENA = "biblioteca123"
clave = input("Ingrese la contraseña de acceso: ")
if clave != CONTRASENA:
    print("Acceso denegado. Contraseña incorrecta.")
else:
    print("Acceso concedido. Bienvenido al sistema secreto.\n")

    # 2. Registrar datos de tres estudiantes
    print("Registro de estudiante 1:")
    nombre1 = input("Nombre: ")
    edad1 = int(input("Edad: "))
    libro1_1 = input("Libro 1: ").strip().title()
    libro1_2 = input("Libro 2: ").strip().title()
    estudiante1 = (nombre1, edad1, [libro1_1, libro1_2])

    print("\nRegistro de estudiante 2:")
    nombre2 = input("Nombre: ")
    edad2 = int(input("Edad: "))
    libro2_1 = input("Libro 1: ").strip().title()
    libro2_2 = input("Libro 2: ").strip().title()
    estudiante2 = (nombre2, edad2, [libro2_1, libro2_2])

    print("\nRegistro de estudiante 3:")
    nombre3 = input("Nombre: ")
    edad3 = int(input("Edad: "))
    libro3_1 = input("Libro 1: ").strip().title()
    libro3_2 = input("Libro 2: ").strip().title()
    estudiante3 = (nombre3, edad3, [libro3_1, libro3_2])

    # Diccionario de estudiantes
    estudiantes = {
        nombre1: estudiante1,
        nombre2: estudiante2,
        nombre3: estudiante3
    }

    # 3. Usar conjuntos para detectar libros repetidos
    set1 = set(estudiante1[2])
    set2 = set(estudiante2[2])
    set3 = set(estudiante3[2])

    repetidos_1_2 = set1 & set2
    repetidos_1_3 = set1 & set3
    repetidos_2_3 = set2 & set3

    libros_repetidos = repetidos_1_2 | repetidos_1_3 | repetidos_2_3

    if libros_repetidos:
        print("\n¡ALERTA! Hay libros repetidos entre estudiantes:")
        if repetidos_1_2:
            print(f"Entre {nombre1} y {nombre2}: {repetidos_1_2}")
        if repetidos_1_3:
            print(f"Entre {nombre1} y {nombre3}: {repetidos_1_3}")
        if repetidos_2_3:
            print(f"Entre {nombre2} y {nombre3}: {repetidos_2_3}")
    else:
        print("\nNo hay libros repetidos entre los estudiantes.")

    # 4. Validar si cada estudiante puede pedir más libros
    autorizado1 = "Autorizado" if edad1 >= 13 else "Denegado"
    autorizado2 = "Autorizado" if edad2 >= 13 else "Denegado"
    autorizado3 = "Autorizado" if edad3 >= 13 else "Denegado"

    # 5. Préstamo especial: libros compartidos y cumple edad mínima
    especial1 = "Aprobado para préstamo especial" if (edad1 >= 13 and (repetidos_1_2 or repetidos_1_3)) else ""
    especial2 = "Aprobado para préstamo especial" if (edad2 >= 13 and (repetidos_1_2 or repetidos_2_3)) else ""
    especial3 = "Aprobado para préstamo especial" if (edad3 >= 13 and (repetidos_1_3 or repetidos_2_3)) else ""

    # 6. Resumen por estudiante
    print("\n--- RESUMEN DE PRÉSTAMOS ---")
    print(f"\nEstudiante: {nombre1}")
    print(f"Edad: {edad1}")
    print(f"Estado de autorización: {autorizado1}")
    if especial1:
        print(especial1)
    print(f"Libros en préstamo (sin repeticiones): {set1}")

    print(f"\nEstudiante: {nombre2}")
    print(f"Edad: {edad2}")
    print(f"Estado de autorización: {autorizado2}")
    if especial2:
        print(especial2)
    print(f"Libros en préstamo (sin repeticiones): {set2}")

    print(f"\nEstudiante: {nombre3}")
    print(f"Edad: {edad3}")
    print(f"Estado de autorización: {autorizado3}")
    if especial3:
        print(especial3)
    print(f"Libros en préstamo (sin repeticiones): {set3}")

    # 7. Total de libros únicos registrados
    total_libros_unicos = set1 | set2 | set3
    print(f"\nTotal de libros únicos registrados entre todos los estudiantes: {len(total_libros_unicos)}")
    print(f"Libros únicos: {total_libros_unicos}")