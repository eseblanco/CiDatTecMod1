
import matplotlib.pyplot as plt
import numpy as np

#plt.ion()  # Ponemos el modo interactivo
plt.scatter(np.random.randn(1000), np.random.randn(1000))
# Dibujamos un graf. dispersion  de valores aleatorios

plt.axvline(-0.5, color = 'g')
# Dibujamos una línea vertical verde centrada en x = -0.5

plt.axvline(-0.5, color = 'g')
# Dibujamos una línea vertical verde centrada en x = 0.5

plt.axhline(-0.5, color = 'g')
# Dibujamos una línea horizontal verde centrada en x = -0.5

plt.axhline(-0.5, color = 'g')
# Dibujamos una línea horizontal verde centrada en x = 0.5

plt.axvspan(-0.5,0.5, alpha = 0.25)
#  Dibujamos un recuadro azul vertical entre x[-0.5,0.5]
#  con transparencia 0.25

plt.axhspan(-0.5,0.5, alpha = 0.25)
#  Dibujamos un recuadro azul horizontal entre x[-0.5,0.5]
#  con transparencia 0.25

plt.show()