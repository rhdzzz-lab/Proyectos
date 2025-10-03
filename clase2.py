import math
#Librerías

nombre = "Roberto"

edad = 25.6

print("El tipo del dato de la variable es:", type(edad))
#type combrueba eñl tipo de dato de una variable

#Print normal
print("Hola", nombre)

#Print f
print(f"Hola {nombre} ¿Cómo estás?\nMuy bien y tu?\nHasta luego")
#\n es un salto de línea

division = 30 / 7

divisionEntera = 30//7

residuo = 30 % 7

print(f"division: {division}\nDivision entera : {divisionEntera}\n Residuio: {residuo}")

coseno = math.cos(45)
calculo = 40 * math.pi
calculo1 = math.sqrt(40 * math.pi)
potencia = math.pow(50 , 3)

print(f"El coseno de 45 es: {coseno}\n Calculo por pi: {calculo}\n El calculo de el diametro es: {calculo1}\n Potencia: {potencia}")
