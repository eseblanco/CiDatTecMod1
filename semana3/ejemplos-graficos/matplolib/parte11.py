

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(25) + 1
# Valores de x

y = np.random.rand(25) * 10.
# Valores de y aleatorios


# y.std()  devuelve la desviacion standar de los valores
# y.mean() Devuelve el promedio de los elementos de la matriz.
# El promedio se toma sobre la matriz plana de forma predeterminada,
#
y_norm = (y - y.mean()) / y.std()

# Valores de y normalizados. Esta nueva serie tiene
# media 0 y desvicación estándar 1 (comprobadlo como ejercicio)

plt.xlim(np.min(x) - 1, np.max(x) + 1)
# Colocamos los límites del eje x

plt.ylim(np.min(y_norm)-1, np.max(y_norm)+1)
# Colocamos los límites del eje y

plt.stem(x[y_norm > 0],y_norm[y_norm > 0], linefmt='k-.', markerfmt='go', basefmt='b-')
# Dibujamos los valores por encima de la media

plt.stem(x[y_norm < 0],y_norm[y_norm < 0], linefmt='k-.', markerfmt='ro', basefmt='b-')
# Dibujamos los valores por debajo de la media

plt.title('Representación de (x, f(x))')
# Colocamos el título del gráfico

plt.xlabel('valores x')
# Colocamos la etiqueta en el eje x

plt.ylabel('valores f(x)')  # Colocamos la etiqueta en el eje y

plt.show()