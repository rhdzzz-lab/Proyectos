print("-" * 30)
print("HOTEL ZETA")
print("-" * 30)

huesped_1 = ("Sofia", "Costa Rica", "A101")
huesped_2 = ("Marco", "Panama", "B202")

# Matriz de pagos
reservas_1 = [
    [75, 80],   # Reserva 1: noche 1 y noche 2
    [0, 0]      # Reserva 2: noche 1 y noche 2 (sin uso)
]

reservas_2 = [
    [66, 65],   # Reserva 1: noche 1 y noche 2
    [70, 0]     # Reserva 2: noche 1 y noche 2
]

#Verifica si ambos huéspedes tienen nacionalidades diferentes
if huesped_1[1] != huesped_2[1]:
    print("✔️ Los huéspedes tienen nacionalidades diferentes.")
else:
    print("❌ Los huéspedes tienen la misma nacionalidad.")

#Muestra el total pagado por el huésped 1
total_sofia = sum(reservas_1[0]) + sum(reservas_1[1])
print(f"Total pagado por {huesped_1[0]}: ${total_sofia}")

#Cambia el número de habitación de Marco por una nueva (reubicación)
huesped_2 = (huesped_2[0], huesped_2[1], "C303")
print(f"Marco ha sido reubicado a la habitación {huesped_2[2]}.")

#Calcula la diferencia entre el segundo pago de Sofía y el primero de Marco
diferencia = reservas_1[0][1] - reservas_2[0][0]
print(f"Diferencia entre el segundo pago de Sofía y el primero de Marco: {diferencia}")

#Muestra si alguno de los huéspedes tiene una noche sin pagar
sin_pagar_sofia = any(pago == 0 for fila in reservas_1 for pago in fila)
sin_pagar_marco = any(pago == 0 for fila in reservas_2 for pago in fila)
if sin_pagar_sofia or sin_pagar_marco:
    print("⚠️ Al menos uno de los huéspedes tiene una noche sin pagar.")
else:
    print("Todos los huéspedes han pagado todas sus noches.")

#Presenta la información final de cada huésped y sus reservas
print("\n--- Información Final ---")
print(f"Huésped 1: {huesped_1}")
print(f"Reservas huésped 1: {reservas_1}")
print(f"Huésped 2: {huesped_2}")
print(f"Reservas huésped 2: {reservas_2}")