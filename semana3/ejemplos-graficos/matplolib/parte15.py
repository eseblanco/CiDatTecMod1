
"""
VER PARTE6 para grafico polar

"""
import matplotlib.pyplot as plt
import numpy as np

#plt.ion()  # Ponemos el modo interactivo
x = np.random.randn(10000)
# Definimos un vector de números aleatorios
# de una distribución normal

plt.hist(x, bins = 20)
# Dibuja un histograma dividiendo el vector x en 20
# intervalos del mismo ancho

plt.show()