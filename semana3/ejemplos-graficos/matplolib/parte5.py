


import matplotlib.pyplot as plt
import numpy as np

#  plt.ion()  # Ponemos la sesión como interactiva si no está como tal
plt.axes()  # Coloca un área de gráfico con los valores por defecto
plt.plot(np.exp(np.linspace(0, 10, 100)))  # Dibuja una exponencial de 0 a 10
# OJAS ESQUINA INFERIOR IZQ ES COORD (0 , 0)
     #valor x,   y , tamaño x ,  y
plt.show()

# queremos borrar el área del gráfico podemos usar
#plt.delaxes()

# queremos borrar el contenido que hay en el área del gráfico podemos usar
#plt.cla()

#si queremos que no aparezca la ‘caja’ donde se dibuja el gráfico
# podemos usar
plt.box()

#queremos que aparezca podemos llamar a
plt.box()

"""
Podemos colocar una rejilla que nos ayude a identificar mejor las 

áreas del gráfico mediante plt.grid() 


"""
plt.grid()

"""
POLAR  ver Parte 6

(en un gráfico polar deberemos usar plt.rgrids() y plt.thetagrids()
"""

"""
matplotlib dibuja los ejes de forma que se ajusten al gráfico pero 

quizá eso no es lo que nos interese en algunos momentos, para ello 

podemos hacer uso de plt.axis()

Nos permite definir la longitud de los ejes, si queremos que aparezcan 
los mismos, si queremos que estos estén escalados
"""



print("final")