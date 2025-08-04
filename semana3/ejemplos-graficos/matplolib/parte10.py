

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(100)
# Valores de x

y = np.random.rand(100)
# Valores de y

plt.plot(x,y, color = 'black', label = '(x, f(x) )')
# Dibujamos la evolución de f(x), frente a x

plt.plot(x[y > 0.9], y[y > 0.9], 'bo', label = 'f(x) > 0.9')
# Destacamos los valores por encima de 0.9 colocándoles un marcador
# circular azul

plt.axhspan(0.9, 1, alpha = 0.1)
# Colocamos una banda de color para los valores f(x) > 0.9

plt.ylim(0,1.2)
# Limitamos el eje x

plt.legend()  # Colocamos la leyenda

plt.title(u'Representación de (x, f(x))')
# Colocamos el título del gráfico

plt.xlabel('valores x')
# Colocamos la etiqueta en el eje x

plt.ylabel('valores f(x)')
# Colocamos la etiqueta en el eje y

plt.show()