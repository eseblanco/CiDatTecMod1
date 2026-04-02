import math
from programa1 import muestreo_normal, muestreo_uniforme

# -----------------------------------------------------------------------------
# PREGUNTAS Y RESPUESTAS
# -----------------------------------------------------------------------------
# 1. ¿Que problema ocurre con el calculo de la funcion de verosimilitud cuando
#    aumentamos la cantidad de observaciones en varios ordenes de magnitud?
# RESPUESTA:
# Ocurre un problema de "Underflow" numerico. Como la verosimilitud es el
# producto de muchas probabilidades (valores entre 0 y 1), el resultado tiende
# a cero muy rapidamente. Con suficientes datos, el valor se vuelve mas pequeno
# que el numero positivo mas pequeno representable por la computadora, y se
# redondea a 0.0, perdiendo toda la informacion.
#
# 2. ¿Cual seria una forma de solucionar este problema?
# RESPUESTA:
# La solucion estandar es utilizar el "Logaritmo de la Verosimilitud"
# (Log-Likelihood). Al aplicar logaritmos, el producto de probabilidades se
# convierte en una suma de log-probabilidades. Esto transforma numeros muy
# pequenos en numeros negativos manejables (ej. ln(10^-100) = -230.2),
# evitando el underflow y facilitando los calculos numericos y la optimizacion.


def calcular_verosimilitud(muestra, mu, sigma):
    """
    Calcula la verosimilitud (likelihood) de que una muestra provenga
    de una distribucion normal con parametros mu y sigma.

    L(mu, sigma | x) = prod( f(x_i | mu, sigma) )
    """
    likelihood = 1.0
    for x in muestra:
        # PDF normal
        term1 = 1 / (sigma * math.sqrt(2 * math.pi))
        term2 = math.exp(-0.5 * ((x - mu) / sigma) ** 2)
        pdf_val = term1 * term2
        likelihood *= pdf_val
    return likelihood


def calcular_log_verosimilitud(muestra, mu, sigma):
    """
    Calcula el Log-Likelihood para evitar problemas numéricos (Underflow).

    l(mu, sigma | x) = sum( ln( f(x_i | mu, sigma) ) )
    """
    log_likelihood = 0.0
    # Constantes pre-calculadas para eficiencia
    const_term = math.log(sigma * math.sqrt(2 * math.pi))

    for x in muestra:
        # ln(pdf) = -ln(sigma * sqrt(2pi)) - 0.5 * ((x-mu)/sigma)^2
        term_exp = 0.5 * ((x - mu) / sigma) ** 2
        log_pdf_val = -const_term - term_exp
        log_likelihood += log_pdf_val

    return log_likelihood


def calcular_mle_normal(muestra):
    """
    Calcula los valores optimos de mu y sigma que maximizan la funcion de
    verosimilitud normal para la muestra dada (Maximum Likelihood Estimation).

    Basado en la teoria (derivada del log-likelihood = 0):
    mu_optima = Promedio(x)
    sigma_optima = sqrt( Promedio( (x - mu_optima)^2 ) )  [Desviacion estandar poblacional/sesgada]
                   (Para N grande es equivalente a la muestral)

    Args:
        muestra (list): Lista de observaciones.

    Returns:
        tuple: (mu_optima, sigma_optima)
    """
    N = len(muestra)
    if N == 0:
        return 0.0, 0.0

    # 1. Calculo de mu (Media Muestral)
    mu_opt = sum(muestra) / N

    # 2. Calculo de sigma (Desviacion estandar poblacional para MLE)
    # Suma de cuadrados de diferencias
    suma_diff_cuadrado = sum((x - mu_opt) ** 2 for x in muestra)

    # Varianza = Suma / N (No N-1, segun definicion estricta de MLE para Normal)
    var_opt = suma_diff_cuadrado / N
    sigma_opt = math.sqrt(var_opt)

    return mu_opt, sigma_opt


def main():
    print("--- Evaluacion de Verosimilitud y MLE ---\n")

    mu_target = 176
    sigma_target = 3

    # -----------------------------------------------------------
    # CASO 1: N Pequeno (50)
    # -----------------------------------------------------------
    # ... (Codigo anterior omitido por brevedad en display, pero mantenido en logica si se requiere) ...
    # Para consistencia con la tarea anterior, mantengo los ejemplos anteriores resumidos o los vuelvo a correr.

    # ... Re-running previous examples quickly
    N_samples = 50
    muestra_normal = muestreo_normal(N_samples, 177, 1)
    muestra_uniforme = muestreo_uniforme(N_samples, 170, 180)
    L_normal = calcular_verosimilitud(muestra_normal, mu_target, sigma_target)
    L_uniforme = calcular_verosimilitud(muestra_uniforme, mu_target, sigma_target)

    # -----------------------------------------------------------
    # CASO 2: N Grande (2000) - Log Likelihood
    # -----------------------------------------------------------
    N_large = 2000
    muestra_grande = muestreo_normal(N_large, 177, 1)
    LL_grande = calcular_log_verosimilitud(muestra_grande, mu_target, sigma_target)
    muestra_uniforme_grande = muestreo_uniforme(N_large, 170, 180)
    LL_uniforme_grande = calcular_log_verosimilitud(
        muestra_uniforme_grande, mu_target, sigma_target
    )

    print(
        f"Log-Likelihood Comparacion (N={N_large}): Normal={LL_grande:.2f} vs Uniforme={LL_uniforme_grande:.2f}"
    )

    # -----------------------------------------------------------
    # CASO 3: MLE (Maximum Likelihood Estimation)
    # -----------------------------------------------------------
    print(f"\n[CASO 3] Estimacion de Parametros Optimos (MLE)")

    # Generamos datos con parametros CONOCIDOS
    mu_real = 170.0
    sigma_real = 5.0
    print(
        f"Generando muestra de N={N_large} con parametros REALES: mu={mu_real}, sigma={sigma_real}"
    )

    muestra_mle = muestreo_normal(N_large, mu_real, sigma_real)

    # Calculamos los parametros optimos recuperados
    mu_estimada, sigma_estimada = calcular_mle_normal(muestra_mle)

    print(f"Parametros estimados por MLE:")
    print(
        f"  mu_estimada:    {mu_estimada:.4f}  (Error: {abs(mu_estimada - mu_real):.4f})"
    )
    print(
        f"  sigma_estimada: {sigma_estimada:.4f}  (Error: {abs(sigma_estimada - sigma_real):.4f})"
    )

    print("\nVerificacion:")
    if abs(mu_estimada - mu_real) < 0.5 and abs(sigma_estimada - sigma_real) < 0.5:
        print("EXITO: Los parametros estimados estan muy cerca de los reales.")
    else:
        print("ALERTA: La estimacion difiere mas de lo esperado.")


if __name__ == "__main__":
    main()
