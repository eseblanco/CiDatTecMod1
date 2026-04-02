import random
from programa1 import muestreo_normal
from programa2 import calcular_mle_normal

# -----------------------------------------------------------------------------
# RESPUESTAS A LAS PREGUNTAS
# -----------------------------------------------------------------------------
# 1. ¿El valor esperado de la varianza aproxima de manera correcta la varianza
#    original de la distribución o es necesario hacer alguna corrección?
#
# RESPUESTA:
# NO aproxima de manera correcta (es "sesgado"). El valor esperado del estimador
# de máxima verosimilitud de la varianza (S^2 = 1/N * sum(x-mu)^2), el cual
# calculamos via `calcular_mle_normal` de programa2, tiende a SUBESTIMAR la
# varianza real de la población.
# Como se observa en la ejecución, para N=30 y sigma^2=1, el promedio obtenido
# es cercano a 0.966, no a 1.0.
#
# 2. Explique cual sería la corrección en caso afirmativo.
#
# RESPUESTA:
# La corrección consiste en multiplicar por el factor de Bessel: N / (N-1).
# Esto transforma la fórmula a: S_unbiased^2 = 1/(N-1) * sum(x-mu)^2.
# En este caso: 0.966 * (30/29) = 1.0.


def main():
    print("--- Demostracion de Sesgo en Estimador de Varianza (Refactorizado) ---\n")

    # Parametros de Generacion
    N_muestras = 10000
    N_obs = 30
    mu_real = 170
    sigma_real = 1
    varianza_real = sigma_real**2

    print(f"Generando {N_muestras} muestras de {N_obs} observaciones cada una...")
    print(
        f"Distribucion Base: Normal(mu={mu_real}, sigma={sigma_real}) -> Varianza Real = {varianza_real}\n"
    )

    # Lista para acumular las varianzas estimadas (sesgadas)
    lista_varianzas_sesgadas = []

    for _ in range(N_muestras):
        # 1. Generar Muestra usando programa1 (Sin Plot!)
        muestra = muestreo_normal(N_obs, mu_real, sigma_real, generar_grafico=False)

        # 2. Calcular MLE usando programa2
        # calcular_mle_normal devuelve (mu_opt, sigma_opt)
        _, sigma_opt = calcular_mle_normal(muestra)

        # La varianza sesgada es sigma_opt^2
        varianza_sesgada = sigma_opt**2

        lista_varianzas_sesgadas.append(varianza_sesgada)

    # 3. Calcular Valor Esperado (Promedio de las varianzas)
    valor_esperado_estimador = sum(lista_varianzas_sesgadas) / N_muestras

    print(f"Resultados:")
    print(f"--------------------------------------------------")
    print(f"Varianza Real (Target):              {varianza_real:.4f}")
    print(f"Promedio de Varianzas Estimadas:     {valor_esperado_estimador:.4f}")

    diferencia = valor_esperado_estimador - varianza_real
    print(f"Diferencia (Sesgo):                  {diferencia:.4f}")

    teorico_esperado = (N_obs - 1) / N_obs * varianza_real
    print(f"Valor Teorico Esperado ((N-1)/N):    {teorico_esperado:.4f}")

    print(f"--------------------------------------------------")

    if abs(valor_esperado_estimador - teorico_esperado) < 0.01:
        print(
            "CONCLUSION: La simulacion confirma la teoria. El estimador esta sesgado."
        )
        print(
            f"            Se obtuvo ~{valor_esperado_estimador:.3f} en lugar de {varianza_real}."
        )
        print(
            f"            Factor de correccion necesario: N/(N-1) = {N_obs}/{N_obs - 1} = {N_obs / (N_obs - 1):.4f}"
        )
        correccion = valor_esperado_estimador * (N_obs / (N_obs - 1))
        print(f"            Varianza corregida: {correccion:.4f}")
    else:
        print("ALERTA: Resultado inseperado.")


if __name__ == "__main__":
    main()
