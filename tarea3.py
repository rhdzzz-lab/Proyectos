#Información del paciente 1
paciente_1 = input("Ingrese el nombre del paciente 1: ")
paciente_1_edad = input("Ingrese la edad del paciente 1: ")
paciente_1_edad = int(paciente_1_edad)
paciente_1_ebais = input("ingrese el Ebáis del paciente 1: ")
paciente_1_altura = input("Ingrese la altura del paciente 1 en metros (Ej: 1.75): ")
paciente_1_altura = float(paciente_1_altura)
paciente_1_peso = input("Ingrese el peso del paciente 1 en kilogramos (Ej: 70.5): ")
paciente_1_peso = float(paciente_1_peso)

#Información del paciente 2
paciente_2 = input("Ingrese el nombre del paciente 2: ")
paciente_2_edad = input("Ingrese la edad del paciente 2: ")
paciente_2_edad = int(paciente_2_edad)
paciente_2_ebais = input("ingrese el Ebáis del paciente 2: ")
paciente_2_altura = input("Ingrese la altura del paciente 2 en metros (Ej: 1.75): ")
paciente_2_altura = float(paciente_2_altura)
paciente_2_peso = input("Ingrese el peso del paciente 2 en kilogramos (Ej: 70.5): ")
paciente_2_peso = float(paciente_2_peso)

#Calcular IMC de los pacientes
imc_paciente_1 = paciente_1_peso / (paciente_1_altura ** 2)
imc_paciente_2 = paciente_2_peso / (paciente_2_altura ** 2)
print(f"El IMC del paciente 1 {paciente_1} es: {imc_paciente_1:.2f}\nEl IMC del paciente 2 {paciente_2} es : {imc_paciente_2:.2f}")

#Comparaciones entre pacientes
edad_mayor = paciente_1_edad > paciente_2_edad
print(f"¿El paciente 1 {paciente_1} es mayor que el paciente 2 {paciente_2}? {edad_mayor}")

nombre_igual = paciente_1 == paciente_2
print(f"¿El paciente 1 {paciente_1} tiene el mismo nombre que el paciente 2 {paciente_2}? {nombre_igual}")

imc_mayor = imc_paciente_1 > imc_paciente_2
print(f"¿El IMC del paciente 1 {paciente_1} es mayor que el del paciente 2 {paciente_2}? {imc_mayor}")

altura = paciente_1_altura > paciente_2_altura
print(f"¿El paciente 1 {paciente_1} es más alto que el paciente 2 {paciente_2}? {altura}")

ebais_igual = paciente_1_ebais == paciente_2_ebais
print(f"¿El Ebáis del paciente 1 {paciente_1} es el mismo que el del paciente 2 {paciente_2}? {ebais_igual}")