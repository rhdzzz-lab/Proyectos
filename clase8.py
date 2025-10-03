#Estrcucturas de datos
"""
Diccionarios
Es una estructura que nos permite
almacenar datos relacionados entre sí. A
diferencia de las listas o tuplas, donde
accedemos a los elementos por su posición,
es un diccionario accedemos 

"""

colores = {"Primarios": "rojo",
           "Secundarios": ["verde", "morado", "anaranjado"],
           "Terciarios" : "gris"}

print(colores["Secundarios"])
print(colores["Secundarios"][1])

usuarios ={"123456789": {"NombreUsuario": "Dylan227", "Contraseña": "1234"},
           "987654321": {"NombreUsuario": "Klyfford", "Contraseña": "5678"}}

diccionarioColores = dict(promarios = "rojo", secundarios = "Verde", terciarios = "gris")
print(diccionarioColores)

persona = {"nombre": "Dylam",
           "colorFavorito" : "Rojo"}
print(persona)
persona["Profesion"] = "Profesor"
print(persona.get("Profesion"))
print(persona.keys())
print(persona.values())
print(persona.items())

"""
Conjuntos/Set
Un conjunto (o set, en ingles) es una estructura de datos muy
parecidad a una lista, pero con dos grandes diferencias:
1. No permite elementos duplicados.
2. No mantiene un orden específico.
Podes imaginarlo como una bolsa magica donde metes elementos,
pero si intenta meter uno que ya estaba, simplemente no lo 
agrega de nuevo.
"""

inventario = ["manzanas", "zanahorias", "atun suli", "atun suli"]
sinRepeticiones = set(inventario)
print(sinRepeticiones)
