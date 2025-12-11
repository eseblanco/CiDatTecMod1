import numpy as np


def generar_muestra(prob_manzana_roja, prob_manzana_azul):
    """
    Genera un punto muestral aleatorio (caja, fruta) basado en las probabilidades dadas usando NumPy.

    Espacio de eventos cajas: Omega1 = {r, a} (roja, azul)
    Espacio de eventos frutas: Omega2 = {n, v} (naranja, manzana verde)

    Probabilidades de cajas (fijas segun el problema):
    P(r) = 0.4
    P(a) = 0.6

    Args:
        prob_manzana_roja (float): Probabilidad de escoger una manzana dado que la caja es roja P(v|r).
        prob_manzana_azul (float): Probabilidad de escoger una manzana dado que la caja es azul P(v|a).

    Returns:
        tuple: (caja, fruta) donde caja en {'r', 'a'} y fruta en {'v', 'n'}
    """

    # 1. Escoger la caja
    # P(r) = 0.4, P(a) = 0.6
    caja = np.random.choice(["r", "a"], p=[0.4, 0.6])

    if caja == "r":
        # Estamos en la caja roja
        # Usamos prob_manzana_roja para decidir la fruta
        fruta = np.random.choice(
            ["v", "n"], p=[prob_manzana_roja, 1 - prob_manzana_roja]
        )
    else:
        # Estamos en la caja azul
        # Usamos prob_manzana_azul para decidir la fruta
        fruta = np.random.choice(
            ["v", "n"], p=[prob_manzana_azul, 1 - prob_manzana_azul]
        )

    return caja, fruta


def generar_caja(n, prob_manzana_roja, prob_manzana_azul):
    """
    Genera una 'caja' (conjunto) de n muestras.

    Args:
        n (int): Numero de muestras a generar.
        prob_manzana_roja (float): P(v|r)
        prob_manzana_azul (float): P(v|a)

    Returns:
        list: Lista de tuplas (caja, fruta)
    """
    muestras = []
    for _ in range(n):
        muestras.append(generar_muestra(prob_manzana_roja, prob_manzana_azul))
    return muestras


if __name__ == "__main__":
    # Datos del problema:
    # Caja Roja: 2 manzanas, 6 naranjas -> Total 8. P(v|r) = 2/8 = 0.25
    # Caja Azul: 3 manzanas, 1 naranja -> Total 4. P(v|a) = 3/4 = 0.75

    p_manzana_r = 2 / 8
    p_manzana_a = 3 / 4

    print(f"Simulacion con NumPy - P(v|r)={p_manzana_r} y P(v|a)={p_manzana_a}")

    # Generar una caja de 10 muestras
    n_muestras = 10
    caja_muestras = generar_caja(n_muestras, p_manzana_r, p_manzana_a)

    print(f"\nGenerando una caja con {n_muestras} muestras:")
    for i, (caja, fruta) in enumerate(caja_muestras):
        print(f"Muestra {i + 1}: Caja={caja}, Fruta={fruta}")
