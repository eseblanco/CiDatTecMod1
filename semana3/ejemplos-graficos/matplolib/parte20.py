
"""
Hasta ahora hemos visto como configurar las ventanas, manejo de las mismas,

definir áreas de gráfico, algunos tipos de gráficos… Ahora vamos a continuar

viendo tipos de gráficos disponibles desde matplotlib.pyplot. En este caso

nos vamos a centrar en otros gráficos que, quizá, sean menos usados que los

 vistos hasta ahora. Algunos ya los hemos visto en otras entradas, como gráficos

 polares, gráficos de contornos

"""
import matplotlib.pyplot as plt
import numpy as np

#ejemplos de gráficos de contornos
x = np.random.rand(20)
# posiciones X de nuestra red de medidas

y = np.random.rand(20)
# posiciones Y de nuestra red de medidas

t = np.random.rand(20)*3000
# valores de Temperatura (ºK) en las posiciones (X, Y)

plt.tricontourf(x, y, t)
# Pintamos las triangulaciones con contornos de color

plt.tricontour(x, y, t, colors = 'k')
# Pintamos las líneas de contorno en color negro

plt.scatter(x, y)


# Pintamos la posición de las estaciones de medida.

plt.show()