#.2f (sirve para mostrar solo dos decimales)
#input(texto) #recibir dato por consola

nombre = input("Ingrese su nombre de usuario: ")
print(f"Hola {nombre}, ¿Cómo estás?")

#int solo acepta números enteros
edad = int(input("Ingrese su edad: "))
edad = int(edad) #Validacion de tipo de dato
#edad = input("Ingrese su edad: ")
print(f"Hola {nombre} tiene {edad} años: {type(edad)}")

#float(dato) convierte un dato a flotante
altura = input("ingrese su altura en Metros: ")
altura = float(altura)
print(f"Hola usuario de estatura de {altura}")

#str(dato) conviete dato a cadena de texto
altura = str(altura)
print(f"Hola usuario de estatura de " + str(altura))

numero1 = input("Usuario 1 ingrese un número: ")
numero1 = int(numero1)

numero2 = input("Usuario 2 ingrese un número: ")
numero2 = int(numero2)

#operaciones relacionales

comparacionIguales = numero1 == numero2
print(f"¿Los números {numero1} y {numero2} son iguales? {comparacionIguales}")

comparacionDiferentes = numero1 != numero2
print(f"¿Los números {numero1} y {numero2} son diferentes? {comparacionDiferentes}")

mayor = numero1 > numero2
print(f"¿El {numero1} es mayor que {numero2}? {mayor}")

menor = numero1 < numero2
print(f"¿El {numero1} es menor que {numero2}? {menor}")

mayorIgual = numero1 >= numero2
print(f"¿{numero1} es mayor o igual que {numero2}? {mayorIgual}")

menorIgual = numero1 <= numero2
print(f"¿{numero1} es menor o igual que {numero2}? {mayorIgual}")

