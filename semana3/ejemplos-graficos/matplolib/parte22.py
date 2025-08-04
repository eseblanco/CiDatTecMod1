


"""
plt.hexbin hace algo parecido a lo anterior pero teniendo en cuenta la ocurrencia
en los intervalos que determinemos (esto mismo lo podemos hacer, por ejemplo, con
plt.matshow aunque tendremos que calcular previamente las frecuencias para cada
recuadro). Vamos a representar el número de veces que los valores de dos series
(x e y) se encuentran en determinado intervalo de datos. Para ello vamos a recurrir,
 como siempre, a np.random.randn:

plt.ion()  # Ponemos el modo interactivo


x = np.random.randn(10000)  # Creamos un vector de 10000 elementos
distribuidos de forma normal
y = np.random.randn(10000)  # Creamos un vector de 10000 elementos distribuidos de
 forma normal
plt.hexbin(x,y, gridsize = 20)  # Representamos como están distribuidos
bidimensionalmente con ayuda de hexbin, en este caso definimos un tamaño del grid
de 20 (esto se puede elegir como se prefiera)
plt.colorbar()  # Colocamos una barra de colores para saber a qué
valor corresponden los colores



"""

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(10000)
# Creamos un vector de 10000 elementos distribuidos de forma normal

y = np.random.randn(10000)
# Creamos un vector de 10000 elementos distribuidos de forma normal

plt.hexbin(x,y, gridsize = 20)
# Representamos como están distribuidos bidimensionalmente con ayuda de hexbin,
# en este caso definimos un tamaño del grid de 20 (esto se puede elegir como
# se prefiera)

plt.colorbar()
# Colocamos una barra de colores para saber a qué valor corresponden los colores

plt.show()