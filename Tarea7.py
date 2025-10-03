# Diccionario inicial
paquetes = {
    "PKG001": {"destino": "San José", "peso": 2.5, "entregado": True},
    "PKG002": {"destino": "Heredia", "peso": 6.1, "entregado": False},
    "PKG003": {"destino": "Cartago", "peso": 4.0, "entregado": False}
}

# 1. Actualiza el estado del paquete "PKG003" a entregado = True
paquetes["PKG003"]["entregado"] = True

# 2. Si el paquete "PKG002" pesa más de 5 kg, agrega la clave "sobrecargo" con el valor "Sí"
if paquetes["PKG002"]["peso"] > 5:
    paquetes["PKG002"]["sobrecargo"] = "Sí"

# 3. Solicita al usuario la información del nuevo paquete "PKG004"
print("\nRegistro de nuevo paquete PKG004:")
destino = input("Ciudad de destino: ")
peso = float(input("Peso en kilogramos: "))
entregado_input = input("¿Ya fue entregado? (sí/no): ").strip().lower()
entregado = True if entregado_input == "sí" else False

# 4. Agrega el paquete "PKG004" al diccionario
paquetes["PKG004"] = {
    "destino": destino,
    "peso": peso,
    "entregado": entregado
}

# 5. Muestra el diccionario final
print("\nDiccionario final de paquetes:")
for codigo, datos in paquetes.items():
    print(f"{codigo}: {datos}")