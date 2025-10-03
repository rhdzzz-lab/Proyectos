# Constantes años de nacimiento y nombres
ANO_NACIMIENTO1 = 2005
ANO_NACIMIENTO2 = 2006
ANO_NACIMIENTO3 = 2007

NOMBRE1 = "juan"
NOMBRE2 = "maria"
NOMBRE3 = "pedro"

# Promedios de estudiantes
promedios1 = [8.5, 8.0, 9.5]
promedios2 = [9.0, 8.5, 9.0]
promedios3 = [7.5, 8.0, 8.5]

# Calcular el promedio
promedio_general1 = sum(promedios1) / len(promedios1)
promedio_general2 = sum(promedios2) / len(promedios2)
promedio_general3 = sum(promedios3) / len(promedios3)

print(f"{NOMBRE1} ({ANO_NACIMIENTO1}) tiene un promedio de {promedio_general1:.2f}")
print(f"{NOMBRE2} ({ANO_NACIMIENTO2}) tiene un promedio de {promedio_general2:.2f}")
print(f"{NOMBRE3} ({ANO_NACIMIENTO3}) tiene un promedio de {promedio_general3:.2f}")

