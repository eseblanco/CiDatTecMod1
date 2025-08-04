

import matplotlib.pyplot as plt
import numpy as np
"""
Hasta ahora hemos visto como podemos configurar la ventana y la sesión,

 en esta ocasión nos vamos a centrar en configurar el área del gráfico.
 
  Para ello vamos a empezar con plt.axes(), que sirve para ‘llamar’ y/o 
  
  configurar a un área de gráfico. Podemos definir la posición, el tamaño, 
  
  el color del área del fondo
"""

import matplotlib.pyplot as plt
import numpy as np

#  plt.ion()  # Ponemos la sesión como interactiva si no está como tal
plt.axes()  # Coloca un área de gráfico con los valores por defecto

ojas = np.linspace(0, 10, 100)
ojas2 = np.exp(ojas)

plt.plot(np.exp(np.linspace(0, 10, 100)))  # Dibuja una exponencial de 0 a 10
# OJAS ESQUINA INFERIOR IZQ ES COORD (0 , 0)
     #valor x,   y , tamaño x ,  y
plt.axes([0.2, 0.55,       0.3, 0.3],
         facecolor='gray')

# Dibuja una nueva área de gráfica colocada y con ancho y
# largo definido por [0.2,0.55,0.3,0.3] y con gris como color de fondo

plt.plot(np.sin(np.linspace(0, 10, 100)), 'b-o', linewidth=2)

plt.show()