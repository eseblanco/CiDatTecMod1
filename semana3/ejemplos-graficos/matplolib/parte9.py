
"""
Revisar mas.  NO MOSTRAR
"""
import matplotlib.pyplot as plt
import numpy as np
import calendar

# dias de un año
dias = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

#dias = [1, 32, 60, 91, 121, 152]
#dias = [np.array(calendar.mdays)[0:i].sum() + 1 for i in np.arange(12)+1]
# Para generar el lugar del primer días de cada mes en un año

meses = calendar.month_name[1:13]
# Creamos una lista con los nombres de los meses
#     posicion x, y
plt.axes(([0.1,0.2,0.8,0.65]))

plt.plot(np.arange(1,366), np.random.rand(365), label = 'valores al azar')
# Creamos un plot con 365 valores

plt.xlim(-5,370)
# Los valores del eje y variarán entre -5 y 370

plt.ylim(0,1.2)
#Los valores del eje y variarán entre 0 y 1.2

plt.legend()
# Creamos la caja con la leyenda

plt.title('Ejemplo de título')  # Ponemos un título

plt.suptitle('Ejemplo de título superior')
# Ponemos un título superior

plt.minorticks_on()
# Pedimos que se vean subrrayas de división en los ejes

plt.xticks(dias, meses, size = 'small', color = 'g', rotation = 45)
# Colocamos las etiquetas, meses, en las posiciones, dias, con color azul
# y rotadas 45º

plt.xlabel('t (días)')

plt.ylabel('Media diaria')

plt.show()