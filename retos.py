# Reto: Pide al usuario un número y muestra si es par o impar.

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")