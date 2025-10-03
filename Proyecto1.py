print("="*60)
print("¡Bienvenido al Proyecto de Recomendación de Películas!")
print("="*60)

# Solicitar nombre de la plataforma
nombre_plataforma = input("¿Cómo quieres llamar a tu plataforma de películas?: ")
print(f"\n¡Bienvenido a {nombre_plataforma}!\n")

# Solicitar estado de ánimo
print("¿Cómo te sientes hoy?")
print("Opciones: Feliz, Triste, Aburrido, Emocionado")
estado_animo = input("Ingresa tu estado de ánimo: ").strip().capitalize()

# Solicitar género preferido
print("\n¿Qué género de película prefieres?")
print("Opciones: Acción, Comedia, Drama, Ciencia ficción, Terror")
genero = input("Ingresa el género de tu preferencia: ").strip().capitalize()

print("\nBuscando la mejor recomendación para ti...\n")

# Recomendaciones usando condicionales anidados
if estado_animo == "Feliz":
    if genero == "Acción":
        print("🎬 Te recomendamos: 'Guardianes de la Galaxia'")
    elif genero == "Comedia":
        print("🎬 Te recomendamos: 'Jumanji: Bienvenidos a la jungla'")
    elif genero == "Drama":
        print("🎬 Te recomendamos: 'En busca de la felicidad'")
    elif genero == "Ciencia ficción":
        print("🎬 Te recomendamos: 'Volver al futuro'")
    elif genero == "Terror":
        print("🎬 Te recomendamos: 'Zombieland'")
    else:
        print("No tenemos recomendaciones para ese género.")
elif estado_animo == "Triste":
    if genero == "Acción":
        print("🎬 Te recomendamos: 'Mad Max: Furia en el camino'")
    elif genero == "Comedia":
        print("🎬 Te recomendamos: 'Un jefe en pañales'")
    elif genero == "Drama":
        print("🎬 Te recomendamos: 'La vida es bella'")
    elif genero == "Ciencia ficción":
        print("🎬 Te recomendamos: 'Interestelar'")
    elif genero == "Terror":
        print("🎬 Te recomendamos: 'El orfanato'")
    else:
        print("No tenemos recomendaciones para ese género.")
elif estado_animo == "Aburrido":
    if genero == "Acción":
        print("🎬 Te recomendamos: 'Rápidos y furiosos'")
    elif genero == "Comedia":
        print("🎬 Te recomendamos: '¿Qué pasó ayer?'")
    elif genero == "Drama":
        print("🎬 Te recomendamos: 'El curioso caso de Benjamin Button'")
    elif genero == "Ciencia ficción":
        print("🎬 Te recomendamos: 'Matrix'")
    elif genero == "Terror":
        print("🎬 Te recomendamos: 'Actividad paranormal'")
    else:
        print("No tenemos recomendaciones para ese género.")
elif estado_animo == "Emocionado":
    if genero == "Acción":
        print("🎬 Te recomendamos: 'Avengers: Endgame'")
    elif genero == "Comedia":
        print("🎬 Te recomendamos: 'Supercool'")
    elif genero == "Drama":
        print("🎬 Te recomendamos: 'Whiplash: Música y obsesión'")
    elif genero == "Ciencia ficción":
        print("🎬 Te recomendamos: 'Ready Player One'")
    elif genero == "Terror":
        print("🎬 Te recomendamos: 'Un lugar en silencio'")
    else:
        print("No tenemos recomendaciones para ese género.")
else:
    print("No reconocemos ese estado de ánimo. Por favor, intenta de nuevo.")

print(f"\nGracias por usar {nombre_plataforma}. ¡Disfruta tu película!")