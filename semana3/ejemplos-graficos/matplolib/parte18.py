"""
https://pybonacci.org/2012/06/23/manual-de-introduccion-a-matplotlib-pyplot-v-tipos-de-grafico-ii/

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10) + 1
y = np.random.rand(10)


#Esta función nos permite dibujar un gráfico de ‘escaleras’.
# Viendo esto en acción entenderéis mejor a lo que me refiero:

plt.step(x, y, where = 'mid', color = 'r', linewidth = 3)

#El where sirve para situar el centro de la escalera
# (trastead con ello, que es gratis)

plt.title("Gráfico ejemplo de 'escaleras'")
plt.xlim(0,11)

plt.show()