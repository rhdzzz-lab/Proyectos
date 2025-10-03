nombre = input("Ingresen su nombre: ")
print(f"Hola {nombre} {type(nombre)}")

edad = input("Ingrese su edad: ")
edad = int(edad)
print(f"Hola {nombre} tienes {edad} años {type(edad)}")

altura = input("Ingrese su altura en metros (Ej: 1.75): ")
altura = float(altura)
print(f"Hola {nombre} de altura {altura} {type(altura)}")

edadMas10 = edad + 10

print(f"Hola {nombre} de edad {edad}, estatura de {altura}." + 
      f"Su edad dentro de 10 años será {edadMas10} ")

