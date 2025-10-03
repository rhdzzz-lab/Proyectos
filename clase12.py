#argumentos - un parametro que recibe una funcion
"""
nombre = "Roberto"

print(nombre.replace("R", "J")) #metodo

def multiplicae10(multiplicador): #parametro
    for i in range(1, 10):
        multiplicacion = multiplicador * i
        print(f"la multiplicacion de {multiplicador} x {i} es: {multiplicacion}")


def insercionDatos():
    for i in range(3):
        nombre = input("ingrese un numero para que se multiplique hasta la tabla del 10: ")

        multiplicae10(int(nombre))

insercionDatos()

"""

def crearUsuarios():
    listaUsuarios = []
    while True:

        opciones = input("Quiere ingresar un usuario\nS = Si\nN = No")

        match opciones.upper():
            case "S":
                usuario = input("Ingrese el nombre de usuario: ")
                listaUsuarios.append(usuario)
            case "N":
                print("Gracias por usar el programa")
                break
    while True:
        opciones = input("Quiere eliminar un usuario\nS = Si\nN = No")

        match opciones.upper():
            case "S":
                eliminarUsuarios(listaUsuarios)
            case "N":
                print("Dejar de ingresar usuarios")
                break

def eliminarUsuarios(listaUsuarios, numero, diccionarios):
    for usuarios in listaUsuarios:
        print(f"{usuarios}")
    usuarioEliminar = input("Que usuario desea eliminar: ")
    listaUsuarios.remove(usuarioEliminar)
    