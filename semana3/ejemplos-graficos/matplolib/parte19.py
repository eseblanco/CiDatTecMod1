


import matplotlib.pyplot as plt
import numpy as np

visitas = [43.97, 9.70, 7.42, 6.68, 3.91, 3.85, 3.62, 3.43, 3.16, 3.04]
visitas2 = [43.97, 9.70, 7.42, 6.68, 3.91]
# Definimos un vector con el % de visitas del top ten de países

visitas = np.append(visitas, 100. - np.sum(visitas))
visitas3 = np.append(visitas2, 100. - np.sum(visitas2))
# Introducimos un último elemento que recoge el % de visitas de otros
# países fuera del top ten

paises = [u'España', u'México', 'Chile', 'Argentina', 'Colombia', 'Ecuador', u'Perú', 'USA', 'Islandia', 'Venezuela', 'Otros']
paises2 = [u'España', u'México', 'Chile', 'Argentina', 'Colombia', 'Otros']
# Etiquetas para los quesitos

explode = [0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0, 0]
explode2 = [0, 0, 0, 0.5, 0.2,0]
# Esto nos ayudará a destacar algunos quesitos
# plt.pie(visitas, labels = paises, explode = explode)  # Dibuja un gráfico de quesitos
# plt.title(u'Porcentaje de visitas por país')

plt.pie(visitas3, labels = paises2, explode = explode2)  # Dibuja un gráfico de quesitos
plt.title('Porcentaje de visitas por país')
plt.show()