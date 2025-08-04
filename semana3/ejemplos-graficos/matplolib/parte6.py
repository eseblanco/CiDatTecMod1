# Grafico polar  verlo al final

import math
## De librerías de terceros

import numpy as np
import matplotlib.pyplot as plt


## Creamos un conjunto de 1000 datos entre 0 y 1 de forma aleatoria
## a partir de una distribución estándar normal

datos = np.random.randn(1000)

## Discretizamos el conjunto de valores en n intervalos,
## en este caso 8 intervalos

datosbin = np.histogram(datos,
bins = np.linspace(np.min(datos), np.max(datos), 9))[0]
#Compute the histogram of a set of data.
# Gráfico de la representación de distribuciones de frecuencias,
# en el que se emplean rectángulos dentro de unas coordenadas


## Los datos los queremos en tanto por ciento

datosbin = datosbin * 100. / len(datos)

"""
En el bloque anterior de código lo único que hemos hecho es obtener 

una muestra aleatoria de una distribución normal y la hemos separado 

en 8 intervalos que pretenden ser las 8 direcciones de donde provienen 

las nubes empezando por el Norte y en el sentido de las agujas del reloj. 

Finalmente los datos los expresamos como frecuencia en tanto por ciento en 

cada una de las 8 direcciones.
"""

"""
Matplotlib nos permite hacer gráficos polares pero estos gráficos 

están pensados para gráficos en sentido contrario a las agujas 

del reloj y empezando a las tres en punto (o al este). 

Por ello debemos modificar como se verán los datos en el 

gráfico polar. Para ello hacemos lo siguiente

"""

## Los datos los queremos en n direcciones/secciones/sectores,
## en este caso usamos 8 sectores de una circunferencia
sect = np.array([90, 45, 0, 315, 270, 225, 180, 135]) * 2. * math.pi / 360.
nombresect = ['E','NE','N','NW','W','SW','S','SE']


## Dibujamos la rosa de frecuencias
plt.axes([0.1,0.1,0.8,0.8], polar = True)

plt.bar(sect, datosbin, align='center', width=45 * 2 * math.pi / 360.,
facecolor='b', edgecolor='k', linewidth=2, alpha=0.5)

plt.thetagrids(np.arange(0, 360, 45),nombresect, fontsize = 10)

plt.title(u'Procedencia de las nubes en marzo')
plt.show()