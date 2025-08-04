
"""
Esos gráficos de contornos se hacen a partir de datos de mallas regulares.

Pero, ¿qué sucede si tenemos datos que están repartidos de forma irregular?

En este caso podemos hacer uso de plt.tricontour y de plt.tricontourf.

Existen unas pocas diferencias de uso con respecto a plt.contour y plt.contourf.

"""
import matplotlib.pyplot as plt
import numpy as np


x = np.sort(np.random.randn(25))
# Valores de x que vamos a usar posteriormente para crear la matriz

y = np.sort(np.random.randn(25))
# Valores de y que vamos a usar posteriormente para crear la matriz

mat1, mat2 = np.meshgrid(x, y)
# Creamos dos matrices cuadradas que vamos a cruzar

mat = np.sqrt( mat1**2 + mat2 **2)
# Creamos una matriz final a partir de las dos anteriores

plt.matshow(mat)  # Representamos la última matriz con matshow
plt.contour(np.arange(25), np.arange(25), mat, 10, colors = 'k')
# Colocamos líneas de contorno para la matriz mat

plt.show()