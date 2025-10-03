# Importamos librerías necesarias 
import math

print("="*60)
print("      SISTEMA DE RECONOCIMIENTO DE IMÁGENES CON IA")
print("="*60)

# Solicitar al usuario la puntuación de confianza
entrada = input("\nIngrese la puntuación de confianza de la IA (0 a 100): ")

# Validación de entrada
if entrada.isdigit():
    puntuacion = int(entrada)
    print(f"\nPuntuación ingresada: {puntuacion}\n")
    
    # Clasificación usando condicionales
    if 90 <= puntuacion <= 100:
        print("✅ Alta confianza, la IA está segura de la clasificación.")
        print("   ¡Sigue así! El modelo está funcionando correctamente.\n")
    elif 70 <= puntuacion <= 89:
        print("🟡 Confianza moderada, pero podría necesitar ajustes.")
        print("   Revisa algunos ejemplos y ajusta parámetros si es necesario.\n")
    elif 50 <= puntuacion <= 69:
        print("🟠 Baja confianza, revisa los datos de entrenamiento.")
        print("   Considera agregar más imágenes o mejorar la calidad de los datos.\n")
    elif 0 <= puntuacion <= 49:
        print("🔴 Muy baja confianza, la IA necesita mejorar significativamente.")
        print("   Es recomendable revisar el modelo y los datos de entrenamiento a fondo.\n")
    else:
        print("⚠️  Puntuación no válida. Debe estar entre 0 y 100.\n")
else:
    print("\n⚠️  Entrada no válida. Por favor, ingrese un número entero entre 0 y 100.\n")

# Comentarios:
# - Se utiliza input() para recibir datos del usuario.
# - Se valida la entrada con isdigit() para evitar errores.
# - Se usan condicionales if, elif, else para clasificar la puntuación.
# - Se agregan líneas y emojis para mejorar la presentación en consola.
# - Se explica cada parte del código con comentarios, como en los ejemplos de clase.