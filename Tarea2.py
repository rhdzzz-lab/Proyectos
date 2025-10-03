import math  #Utilizando libreria math

#Todos las operaciones matemáticas utlizadas son proporcionada por la librería math
"""Como parte del codigo en cada operación matemática se utilizaron f-strings para
mostrar todas las salidas de manera ordenada y clara, además de mostar el tipo de dato"""

raiz = math.sqrt(25)
print(f"La raíz cuadrada de 25 es: {raiz}\nEl tipo del dato de la variable es: {type(raiz)}\n")

potencia = math.pow(5, 3)
print(f"La potencia de 5^3 es: {potencia}\nEl tipo del dato de la variable es: {type(potencia)}\n")

valorabsoluto = math.fabs(-15)
print(f"El valor absoluto de -15 es: {valorabsoluto}\nEl tipo del dato de la variable es: {type(valorabsoluto)}\n")

logbase10 = math.log10(1000)
print(f"El logaritmo base 10 de 1000 es: {logbase10}\nEl tipo del dato de la variable es: {type(logbase10)}\n")

factorial = math.factorial(6)
print(f"El factorial de 6 es: {factorial}\nEl tipo del dato de la variable es: {type(factorial)}\n")

"""Para calculo el seno y coseno primero utilizanso la funcion math.radians
para convertir grados a radianes para posteriormente calcular el seno y coseno
con un valor en radianes."""
grados = 45
radianes = math.radians(grados)
seno = math.sin(radianes)
coseno = math.cos(radianes)
print(f"El seno de 45 es: {seno}\nEl tipo del dato de la variable es: {type(seno)}\n")
print(f"El coseno de 45 es: {coseno}\nEl tipo del dato de la variable es: {type(coseno)}\n")

maxComunDivisor = math.gcd(56, 98)
print(f"El máximo común divisor de 56 y 98 es: {maxComunDivisor}\nEl tipo del dato de la variable es: {type(maxComunDivisor)}\n")

pi = math.pi
print(f"El valor de pi es: {pi: .2f}\nEl tipo del dato de la variable es: {type(pi)}\n")

e = math.e
print(f"El valor de e es: {e: .2f}\nEl tipo del dato de la variable es: {type(e)}\n")