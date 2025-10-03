# Tupla: Una tupla es una colección e inmutable.
# Se usa para agrupar datos relacionados.

"""
- las tuplas usan parenteisis ()
- cada elemento se separa con coma
- los ele,emtos pueden ser nu,eros, textos, booleanos o mezclas
- el primer elemento siempre es la posicion 0, el segundo en la 1, y asi sucesivamente
- las tuplas son inmutables, es decir, no se pueden modificar
"""

"""
roles = ("Administrador", "Administrador", "Invitado", "Cliente")

empleados = ["Danyy", "Dylan"]
empleados.append("Joshua")
#print(f"El rol numero  en el sistema es: {roles[0]}")

estados = ("Activo", "Inactivo", "Sin stock", "Proximo a vencer")

producto = estados[1]
print(f"En el sistema hay {len(estados)} estados almacenados")

empeados = tuple(empleados)

if "Dylan" in empleados:
    print("Hola Dylan esta en la lista de empleados")


if "Dylan" not in empleados:
    print("Hola Dylan no esta en la lista de empleados")

print(roles.count("Administrador"))

print(roles.index("Administrador"))

"""

mascota_1 = ("Max", "perro", 3, "marrón", True)
mascota_2 = ("Michi", "gato", 2, "gris", False)

print(f"Mi mascota se llama {mascota_1[0]}, es un {mascota_1[1]}.\nSe encuentra vacunado: {mascota_1[4]}\nLa mascota esta lista para consulta.")
print(f"Mi mascota se llama {mascota_2[0]}, es un {mascota_2[1]}.\nSe encuentra vacunado: {mascota_2[4]}\nDebe vacunarse antes de la consulta.")

edad_1 = mascota_1[2] <= 1 or mascota_1[2] >=1 or mascota_1[2] >=6
print(f"La mascota {mascota_1[0]} tiene {mascota_1[2]} años por lo tanto es {edad_1}.")

"""
Matriz: Una matriz en Python no es un tipo de dato propio,
sino que se representa como una lista de listas, es
decir, una lista donde cada elemento también es
una lista.
- las matrices en python se representan como lista de listas
- cada fila es una lista interna, y todad estan dento de una lista externa
- 
"""

colores = [
    ["Rojo", "Amarillo", "Azul"],
    ["Anaranjado", "Verde", "Morado"],
    ["Cafe", "Turquesa", "Cyan"]
]

print(colores[0][2])
print(colores[0])
print(colores)

colores[0].append("Gris")
colores[1][1] = "Blanco"

colores2 = colores.copy()

print(len(colores[0]))