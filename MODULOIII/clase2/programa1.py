import random
import matplotlib.pyplot as plt


def muestreo_uniforme(N, min_height, max_height, generar_grafico=True):
    """
    Genera N observaciones de una distribucion uniforme y muestra un histograma.
    Retorna la lista de estaturas generadas.
    """
    estaturas = [random.uniform(min_height, max_height) for _ in range(N)]

    if generar_grafico:
        plt.figure(figsize=(8, 6))
        plt.hist(estaturas, bins=9, color="skyblue", edgecolor="black")
        plt.title(f"Muestreo Uniforme (N={N}, min={min_height}, max={max_height})")
        plt.xlabel("Estatura (cm)")
        plt.ylabel("Frecuencia")
        plt.grid(True, alpha=0.3)
        # Save specifically for headless verification, user can see it in file system
        plt.savefig("histograma_uniforme.png")
        print("Histograma uniforme guardado como 'histograma_uniforme.png'")
        # show() might block in some environments or be useless in headless,
        # but good to have for user running locally.
        # plt.show()
        plt.close()

    return estaturas


def muestreo_normal(N, mean, std_dev, generar_grafico=True):
    """
    Genera N observaciones de una distribucion normal y muestra un histograma.
    Retorna la lista de estaturas generadas.
    """
    estaturas = [random.gauss(mean, std_dev) for _ in range(N)]

    if generar_grafico:
        plt.figure(figsize=(8, 6))
        plt.hist(estaturas, bins=9, color="lightgreen", edgecolor="black")
        plt.title(f"Muestreo Normal (N={N}, media={mean}, desv={std_dev})")
        plt.xlabel("Estatura (cm)")
        plt.ylabel("Frecuencia")
        plt.grid(True, alpha=0.3)
        plt.savefig("histograma_normal.png")
        print("Histograma normal guardado como 'histograma_normal.png'")
        # plt.show()
        plt.close()

    return estaturas


if __name__ == "__main__":
    # Ejemplo Muestreo Uniforme
    print("--- Ejemplo Muestreo Uniforme ---")
    uniformes = muestreo_uniforme(100, 150, 168)
    print(f"Primeras 10 estaturas uniformes: {uniformes[:10]}")
    print("\n")

    # Ejemplo Muestreo Normal
    print("--- Ejemplo Muestreo Normal ---")
    # Asumiendo una media de 170cm y desviacion estandar de 10cm
    normales = muestreo_normal(100, 170, 10)
    print(f"Primeras 10 estaturas normales: {normales[:10]}")
