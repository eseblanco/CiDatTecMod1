



import matplotlib.pyplot as plt
import numpy as np
import datetime as dt  # Importamos el módulo datetime


plt.axes((0.2,0.1,0.7,0.8))
# Creamos los ejes en la posición que queremos

plt.title('Evolución para hoy de los tipos de nubosidad')
# Ponemos un título al gráfico

plt.broken_barh([(0,1),(3,3), (10,5), (21,3)], (9500, 1000))
# Dibujamos los momentos en que ha habido nubes altas

plt.broken_barh([(0,24)], (4500, 1000))
# Dibujamos los momentos en que ha habido nubes medias

plt.broken_barh([(0,9), (12,5), (20,2)], (1500, 1000))
# Dibujamos los momentos en que ha habido nubes bajas

plt.xlim(-1,25)  # Limitamos el rango de valores del eje x

plt.yticks([2000, 5000, 10000], ['nubes bajas', 'nubes medias',
                                 'nubes altas'])
# Colocamos etiquetas en el eje y

plt.xlabel('t(h)')
# Y finalmente ponemos un título al eje x, el eje de tiempos

plt.show()
