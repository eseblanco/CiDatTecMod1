
"""
Por último por hoy vamos a dibujar gráficos de flechas.

Esto se suele usar para dibujar viento, el movimiento de un fluido,

movimiento de partículas, … En este caso vamos usar plt.quiver

(echadle un ojo también a plt.quiverkey y a plt.barbs).

"""

import matplotlib.pyplot as plt
import numpy as np


lon = np.arange(15) - 10.
# Creamos un vector de longitudes

lat = np.arange(15) + 30.
# Creamos un vector de latitudes

lon2, lat2 = np.meshgrid(lon, lat)
# Creamos un array 2D para las longitudes y latitudes

lon = lon2
lat = lat2

u = np.random.randn(15 * 15)
# Componente x del vector viento que partirá desde una lon y una lat determinada

v = np.random.randn(15 * 15)
# Componente y del vector viento que partirá desde una lon y una lat determinada

colores = ['k','r','b','g','c','y','gray']
#  Definimos una serie de colores para las flechas

plt.title('Flechas de un viento un poco loco')
# Colocamos un títuloplt

plt.xlabel('longitud')
# Colocamos la etiqueta para el efe x

plt.ylabel('latitud')
# Colocamos la etiqueta para el eje y

plt.quiver(lon, lat, u, v, color = colores)
# Dibujamos las flechas 'locas'

plt.show()