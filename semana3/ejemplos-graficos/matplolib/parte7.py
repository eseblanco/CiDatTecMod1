


import matplotlib.pyplot as plt
import numpy as np


# plt.ion()
plt.plot(np.arange(100), 'b')
# Dibujamos una línea recta azul

plt.xlabel('Valores de x')
# Ponemos etiqueta al eje x

plt.ylabel('Línea azul')
# Ponemos etiqueta al eje y

plt.twinx()
# Creamos un segundo eje y

plt.plot(np.exp(np.linspace(0,5,100)), 'g')
# Dibuja una exponencial de 0 a 5 con la y representada
# en el segundo eje y

plt.ylabel('Línea verde')
# Ponemos etiqueta al segundo eje y

plt.xlim(-10,110)
# Limitamos los valores del eje x para que vayan desde -10 a 110

plt.show()




print("final")