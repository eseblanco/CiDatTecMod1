"""
Una prueba de diagnóstico para una enfermedad es tal que (correctamente) detecta la enfermedad en
90% de los individuos que en realidad tienen la enfermedad. También, si una persona no tiene la enfermedad,
la prueba reportará que él o ella no la tiene con probabilidad 0.9. Sólo 1% de la población tiene la enfermedad en cuestión.
Si una persona es seleccionada al azar de la población y la prueba de diagnóstico indica que tiene la enfermedad,
¿cuál es la probabilidad condicional de que tenga, en realidad, la enfermedad?
"""
# T: prueba
# D: enfermedad
# ~D: no enfermedad
# T: positivo
# ~T: negativo

# Datos del problema
p_enfermedad = 0.01  # P(D)
p_no_enfermedad = 1 - p_enfermedad  # P(~D)

p_positivo_dado_enfermedad = 0.90  # P(T|D)
p_negativo_dado_no_enfermedad = 0.90  # P(~T|~D)
p_positivo_dado_no_enfermedad = 1 - p_negativo_dado_no_enfermedad  # P(T|~D)

# Teorema de Bayes: P(D|T) = P(T|D) * P(D) / P(T)
# Donde P(T) = P(T|D) * P(D) + P(T|~D) * P(~D)

p_positivo = (p_positivo_dado_enfermedad * p_enfermedad) + (
    p_positivo_dado_no_enfermedad * p_no_enfermedad
)

p_enfermedad_dado_positivo = (p_positivo_dado_enfermedad * p_enfermedad) / p_positivo

print(
    f"La probabilidad de tener la enfermedad dado que la prueba es positiva es: {p_enfermedad_dado_positivo:.4f}"
)
