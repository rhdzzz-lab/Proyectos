import numpy as np
import matplotlib.pyplot as plt

# ------------------ CONFIG ------------------
RANGO_AUTO_INI = -15
RANGO_AUTO_FIN = 25
PUNTOS_AUTO = 120
CANTIDAD_MANUAL = 30
# --------------------------------------------

def pedir_opcion():
    """Devuelve 0 si el usuario quiere ingresar manualmente, 1 si quiere generar automáticamente."""
    while True:
        try:
            op = int(input("¿Deseas ingresar (0) o generar (1) los valores de x? [0/1]: ").strip())
            if op in (0, 1):
                return op
        except ValueError:
            pass
        print("❌ Opción inválida. Escribe 0 o 1.")

def leer_x_manual(n=CANTIDAD_MANUAL):
    """Lee n valores separados por comas y regresa un np.array."""
    while True:
        entrada = input(f"Ingresea {n} valores de x separados por comas: ").strip()
        try:
            valores = [float(v) for v in entrada.split(",")]
        except ValueError:
            print("❌ Asegúrate de ingresar solo números separados por comas.")
            continue

        if len(valores) != n:
            print(f"⚠ Debes ingresar exactamente {n} valores (recibidos: {len(valores)}).")
            continue
        return np.array(valores, dtype=float)

def generar_x(ini=RANGO_AUTO_INI, fin=RANGO_AUTO_FIN, puntos=PUNTOS_AUTO):
    """Genera un vector x equiespaciado."""
    if fin <= ini:
        # salvaguarda por si alguien cambia los valores arriba
        fin = ini + 1
    return np.linspace(ini, fin, puntos, dtype=float)

def graficar(x):
    """Calcula y=2x+4 y grafica."""
    y = 2 * x + 4
    plt.figure()
    plt.plot(x, y, label="y = 2x + 4")  # sin colores específicos
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfica de y = 2x + 4")
    plt.grid(True)
    plt.legend()
    try:
        plt.show(block=True)
    except TypeError:
        plt.show()

def main():
    continuar = "si"
    while continuar == "si":
        opcion = pedir_opcion()
        if opcion == 0:
            x = leer_x_manual()
        else:
            # Puedes pedir al usuario si quiere cambiar los valores por defecto.
            # Para mantenerlo simple, usamos la configuración de arriba.
            x = generar_x()

        graficar(x)
        continuar = input("¿Desea continuar con otro conjunto? (si/no): ").strip().lower()

    print("Programa finalizado.")

if __name__ == "__main__":
    main()
