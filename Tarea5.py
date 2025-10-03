print("|-|"*15)
print("BIENVENIDO A RUBEN EL ADMINISTRADOR DE TAREAS")
print("|-|"*15)

nombre = input(f"Bienvenido ingrese su nombre: ")
print(f"Hola {nombre} bienvenido a Ruben tu administrador de tareas")

while True:
    opciones = input(
        "\nMenu de opciones:\n"
        "1. Anotar una tarea\n"
        "2. Eliminar una tarea concluida\n"
        "3. Organizarte mejor (ordenar, invertir, etc.)\n"
        "4. Mostrar lista\n"
        "5. Borrar la lista de tareas\n"
        "6. Buscar tarea (index y count)\n"
        "7. Salir del sistema\n"
    )
    if opciones.isdigit():
        opciones = int(opciones)
        match opciones:
            case 1:
                tarea = input("Ingrese la tarea que desea anotar: ")
                if tarea:
                    with open("tareas.txt", "a") as file:
                        file.write(tarea + "\n")
                    print(f"Tarea '{tarea}' anotada exitosamente.")
                else:
                    print("La tarea no puede estar vacía. Intente nuevamente.")
            case 2:
                tarea_eliminar = input("Ingrese la tarea que desea eliminar: ")
                try:
                    with open("tareas.txt", "r") as file:
                        tareas = [t.strip() for t in file.readlines()]
                    if tarea_eliminar in tareas:
                        tareas.remove(tarea_eliminar)
                        with open("tareas.txt", "w") as file:
                            for t in tareas:
                                file.write(t + "\n")
                        print(f"Tarea '{tarea_eliminar}' eliminada exitosamente.")
                    else:
                        print("La tarea no se encontró en la lista.")
                except FileNotFoundError:
                    print("No hay tareas registradas.")
            case 3:
                try:
                    with open("tareas.txt", "r") as file:
                        tareas = [t.strip() for t in file.readlines()]
                    if not tareas:
                        print("No hay tareas registradas para organizar.")
                        continue
                    print("\nOpciones de organización:")
                    print("a) Ordenar alfabéticamente (A-Z)")
                    print("b) Ordenar alfabéticamente inverso (Z-A)")
                    print("c) Invertir el orden actual")
                    print("d) Limpiar toda la lista (clear)")
                    subop = input("Elige una opción (a/b/c/d): ").lower()
                    if subop == "a":
                        tareas.sort()
                        print("Tareas ordenadas alfabéticamente (A-Z).")
                    elif subop == "b":
                        tareas.sort(reverse=True)
                        print("Tareas ordenadas alfabéticamente (Z-A).")
                    elif subop == "c":
                        tareas.reverse()
                        print("Tareas invertidas.")
                    elif subop == "d":
                        tareas.clear()
                        print("Lista de tareas vaciada con clear().")
                    else:
                        print("Opción no válida.")
                        continue
                    with open("tareas.txt", "w") as file:
                        for t in tareas:
                            file.write(t + "\n")
                except FileNotFoundError:
                    print("No hay tareas registradas para organizar.")
            case 4:
                try:
                    with open("tareas.txt", "r") as file:
                        tareas = [t.strip() for t in file.readlines()]
                    if tareas:
                        print("Lista de Tareas:")
                        for i, t in enumerate(tareas, start=1):
                            print(f"{i}. {t}")
                    else:
                        print("No hay tareas registradas.")
                except FileNotFoundError:
                    print("No hay tareas registradas.")
            case 5:
                confirmacion = input("¿Está seguro de que desea borrar todas las tareas? (si/no): ")
                if confirmacion.lower() == 'si':
                    with open("tareas.txt", "w") as file:
                        pass
                    print("Todas las tareas han sido borradas.")
                else:
                    print("Operación cancelada.")
            case 6:
                try:
                    with open("tareas.txt", "r") as file:
                        tareas = [t.strip() for t in file.readlines()]
                    if tareas:
                        buscar = input("Ingrese la tarea que desea buscar: ")
                        cantidad = tareas.count(buscar)
                        if cantidad > 0:
                            indice = tareas.index(buscar)
                            print(f"La tarea '{buscar}' aparece {cantidad} vez/veces. Primera posición: {indice+1}")
                        else:
                            print("La tarea no se encontró en la lista.")
                    else:
                        print("No hay tareas registradas.")
                except FileNotFoundError:
                    print("No hay tareas registradas.")
            case 7:
                print("Saliendo del sistema...\nGracias por usar Ruben, su administrador de tareas. ¡Vuelva pronto!")
                break
    else:
        print("Por favor, ingrese solo números del 1 al 7.")