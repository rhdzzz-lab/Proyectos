print("-" * 30)
print("Tienda de Ropa")
print("-" * 30)

ventas = [
    [10, 12],
    [5, 8],
    [3, 4]
]

#1
print(f"Camisetas vendidas el segundo día: {ventas[0][1]}")

# 2
ventas[1][0] = 7

# 3
total_chaquetas = ventas[2][0] + ventas[2][1]
print(f"Total de chaquetas vendidas en los dos días: {total_chaquetas}")

# 4
total_dia1 = ventas[0][0] + ventas[1][0] + ventas[2][0]
print(f"Total de prendas vendidas el primer día: {total_dia1}")

# 5
print("Matriz final de ventas:")
print(ventas)