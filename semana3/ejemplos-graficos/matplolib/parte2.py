
import matplotlib.pyplot as plt
import numpy as np

plt.ioff()  # Nos ponemos en modo interactivo
         # filas, cols, fila selecc
plt.subplot(1,   2,       1)
# Dividimos la ventana en una fila y dos columnas y dibujamos el primer gráfico
plt.plot((1,2,3,4,5))
# filas, cols, fila selecc
plt.subplot(1,    2,      2)  # Dividimos la ventana en una fila y dos columnas y dibujamos el segundo gráfico
plt.plot((5,4,3,2,1))
plt.show()
