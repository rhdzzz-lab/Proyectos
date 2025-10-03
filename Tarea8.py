print("-" * 17)
print("Áreas de interés")
print("-" * 17)

# Solicitar áreas de interés para Colegio A
areas_a = set()
print("Ingrese tres áreas de interés para el Colegio A:")
for i in range(1, 4):
    area = input(f"Área {i} Colegio A: ").strip().capitalize()
    areas_a.add(area)

# Solicitar áreas de interés para Colegio B
areas_b = set()
print("\nIngrese tres áreas de interés para el Colegio B:")
for i in range(1, 4):
    area = input(f"Área {i} Colegio B: ").strip().capitalize()
    areas_b.add(area)

# 1. Guarda los intereses en conjuntos (ya realizado arriba)

# 2. Muestra las áreas comunes entre ambos colegios
comunes = areas_a & areas_b
print(f"\nÁreas comunes entre ambos colegios: {comunes}")

# 3. Muestra las áreas que solo interesan al Colegio A
solo_a = areas_a - areas_b
print(f"Áreas que solo interesan al Colegio A: {solo_a}")

# 4. Muestra todas las áreas únicas registradas
todas_unicas = areas_a | areas_b
print(f"Todas las áreas únicas: {todas_unicas}")