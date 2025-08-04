"""

para instalar  matplolib

pip install matplotlib

https://pythonspot.com/matplotlib/

"""

import matplotlib.pyplot as plt
"""
módulo ----pyplot---- de matplotlib se suele usar para hacer 
pruebas rápidas desde la línea de comandos, programitas cortos
 o programas donde los gráficos serán, en general, sencillos
"""


import matplotlib.pyplot as plt
import numpy as np

"""
Muchos de los gráficos que vamos a representar no tienen ningún 

sentido físico y los resultados solo pretenden mostrar el 

uso de la librería



Normalmente, cuando iniciamos la sesión, esta no está puesta
 
en modo interactivo. En modo interactivo, cada vez que metemos 

código nuevo relacionado con el gráfico o la ventana 

(recordad, una instancia de matplotlib.axes.Axes 

o de matplotlib.figure.Figure, respectivamente), 

este se actualizará. 

Cuando no estamos en modo interactivo, el gráfico no se actualiza hasta
 
 que llamemos a show() 
 (si no hay una ventana abierta) o draw() 
 
 (normalmente no lo usaréis para nada) explícitamente. 
 
 Veamos como es esto:
"""

# nos devolverá false pues no esta en modo interactivo.
#
# print(plt.isinteractive())

"""
Esto significa que si hacemos lo siguiente:

"""

# plt.plot([1,2,3,4,5])

# no lanzara una ventana hasta que se haga.

#plt.show()

"""  para hacer cambios del modo interactivo se utiliza """
#
# plt.ion() #  inicia el modo interactivo
#
# print(plt.isinteractive())
#
# plt.ioff() # apaga el modo interactivo
#
# print(plt.isinteractive())

# antes de lo siguiente comentar todo lo anterior.
# plt.ion()
# plt.plot([1, 2, 3, 4])


"""
queremos cerrar la ventana podemos usar plt.close().
"""

# plt.close()
#
# plt.ioff()

# ya en un programa
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

