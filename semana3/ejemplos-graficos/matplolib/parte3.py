
import matplotlib.pyplot as plt
import numpy as np

plt.ioff()  # Nos ponemos en modo interactivo

plt.figure('valores por defecto')
# Creamos una ventana donde dibujamos el gráfico con
# la configuración por defecto

plt.suptitle('Titulo valores por defecto')
# Esto sirve para poner título dentro de la ventana

plt.plot((1,2,3,4,5), label = 'por defecto')
# Hacemos el plot

plt.legend(loc = 4)
# Colocamos la leyenda en la esquina superior izquierda




plt.rc('lines', linewidth = 2)
# A partir de aquí todas las líneas que dibujemos irán con ancho doble

plt.rc('font', size = 18)
# A partir de aquí las fuentes que aparezcan en cualquier gráfico en la
# misma sesión tendrán mayor tamaño

plt.figure('valores modificados')
# Creamos una ventana donde dibujamos el gráfico con la
# configuración por defecto

plt.suptitle('Titulo valores modificados')
# Esto sirve para poner título dentro de la ventana

plt.plot((1,2,3,4,5), label = 'linea más ancha y letra más grande')
# Hacemos el plot

plt.legend(loc = 2)
# Colocamos la leyenda en la esquina superior izquierda


plt.show()