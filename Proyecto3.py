print("-*-" * 9)
print("SISTEMA DE CALIFICACIONES")
print("-*-" * 9)

nombre_profesor = input("Hola profesor, ingrese su nombre: ")
print(f"Hola profesor {nombre_profesor}, bienvenido al sistema de calificaciones\n")

# Lista para almacenar si cada estudiante aprobó o no
aprobados = []

for i in range(1, 4):
    print(f"\nIngrese los datos del estudiante {i}:")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    curso = input("Curso matriculado: ")
    nota = input("Nota final (0-100): ")

    edad = int(edad)
    nota = float(nota)

    print(f"\nDatos del estudiante {i}:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Curso: {curso}")
    print(f"Nota final: {nota}")

    # Determinar si aprueba o reprueba
    if nota >= 70:
        print("Estado: Aprobado ✅")
        aprobados.append(True)
    else:
        print("Estado: Reprobado ❌")
        aprobados.append(False)

if all(aprobados):
    print("\n¡Todos los estudiantes aprobaron! 🎉")
else:
    print("\nHay estudiantes que deben repetir el curso.")