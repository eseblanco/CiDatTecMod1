
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(25) + 1
# Valores de x

y1 = np.random.rand(25) * 10.
# Valores de y1

y2 = np.random.rand(25) * 10.
# Valores de y2

plt.xlim(np.min(x) - 1, np.max(x) + 1)
# Colocamos los límites del eje x

plt.ylim(np.min([y1, y2])-1, np.max([y1, y2])+1)
# Colocamos los límites del eje y

plt.plot(x, y1, 'k-', linewidth = 2, label = 'Serie 1')
# Dibujamos los valores de (x,y1) con una línea contínua

plt.plot(x, y2, 'k-.', linewidth = 2, label = 'Serie 2')
# Dibujamos los valores de (x,y2) con una línea de punto y raya

plt.fill_between(x, y1, y2, where = (y1 < y2), color = 'g', interpolate = True)
# Pinta polígonos color verde entre las líneas cuando y1 < y2

plt.fill_between(x, y1, y2, where = (y1 > y2), color = 'r', interpolate = True)
# Pinta polígonos color rojo entre las líneas cuando y1 > y2

plt.legend()
plt.title('Ejemplo de plt.fill_between()')
# Colocamos el título del gráfico

plt.xlabel('valores x')
# Colocamos la etiqueta en el eje x

plt.ylabel('valores y')
# Colocamos la etiqueta en el eje y

plt.show()