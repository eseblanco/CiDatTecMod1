"""

para instalar  matplolib

pip install matplotlib

https://pythonspot.com/matplotlib/

"""


import matplotlib.pyplot as plt
import numpy as np

plt.figure('Una FIgura') # Crea una ventana titulada 'Una FIgura'
plt.figure('grafico')    # Crea una ventana titulada 'grafico'

a = np.random.rand(100) # Generamos un vector de valores aleatorios
b = np.random.rand(100) # Generamos otro vector de valores aleatorios
print(a)
print(b)
plt.figure('Una FIgura') # Le decimos que la ventana activa en la que vamos a dibujar
# es la ventana 'scatter'
# 'scatter' = dispersion
plt.scatter(a,b)  # Dibujamos un scatterplot en la ventana 'scatter'
plt.show()
plt.figure('grafico') # Ahora cambiamos a la ventana 'plot'
plt.plot(a,b)
plt.show()
plt.close()



"""
queremos borrar todos los gráficos (matplotlib.axes.Axes), 

títulos, …, de la ventana (matplotlib.figure.Figure) 

podemos usar plt.clf() y nos volverá a dejar el ‘lienzo’ limpio

"""
plt.clf()

# from numpy import pi
# from numpy.ma import arange, sin
#
# from pylab import *
# t = arange(0.0, 2.0, 0.01)
# s = sin(2.5*pi*t)
# plot(t, s)
#
# xlabel('time (s)')
# ylabel('voltage (mV)')
# title('Sine Wave')
# grid(True)
# show()

