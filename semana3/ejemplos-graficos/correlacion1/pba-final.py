

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

print(os.getcwd())
df = pd.read_csv(os.getcwd()+os.sep+"frac-Adver1.csv")

df2 = pd.read_csv(os.getcwd()+os.sep+"frac-Adver2.csv")



df3 = pd.merge(df,df2)

print(df3)

print(df3['TV'].corr(df3['Sales']))
print(df3['Radio'].corr(df3['Sales']))
print(df3['Newspaper'].corr(df3['Sales']))

result = []
result.append(df3['TV'].corr(df3['Sales']))
result.append(df3['Radio'].corr(df3['Sales']))
result.append(df3['Newspaper'].corr(df3['Sales']))
etiquetas=['TV', 'Radio','Periodico']

plt.axes((0.1, 0.3, 0.8, 0.6))  # Definimos la posición de los ejes
plt.bar( np.arange(3),result)
# plt.ylim(0,1)  # Limitamos los valores del eje y al range definido [450, 550]
plt.title('Correlacion con las Ventas')  # Colocamos el título
plt.xticks(np.arange(3), etiquetas, rotation = 45)  # Colocamos las etiquetas del eje x, en este caso, las fechas

# plt.plot(result, label = 'Correlacion')
plt.show()

#
#
# import datetime as dt  # Importamos el módulo datetime
#
#
# prima = 600 + np.random.randn(5) * 10  # Valores inventados para la prima de riesgo
# fechas = (dt.date.today() - dt.timedelta(5)) + dt.timedelta(1) * np.arange(5) # generamos las fechas de los últimos cinco días
# plt.axes((0.1, 0.3, 0.8, 0.6))  # Definimos la posición de los ejes
# plt.bar(np.arange(5), prima)  # Dibujamos el gráfico de barras
# plt.ylim(550,650)  # Limitamos los valores del eje y al range definido [450, 550]
# plt.title('prima de riesgo')  # Colocamos el título
# plt.xticks(np.arange(5), fechas, rotation = 45)  # Colocamos las etiquetas del eje x, en este caso, las fechas
# # print(df3.corr())

