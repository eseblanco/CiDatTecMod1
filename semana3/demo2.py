
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# hay que instalar python -m pip install PyQt5
matplotlib.use('Qt5Agg')

separador = "-"*40
archivo = "/home/sblanco/Documentos/PycharmProjects/CienciaDatosTEC/semana3/Dataset_usar.csv"

# carga el archivo en pandas
dataFrame = pd.read_csv(archivo, header = 0, delimiter=';')

# guarda el nombre de las columnas en una lista
colNames = dataFrame.columns

# muestra los primeros elementos del dataFrame
print(separador)
print("Datos en dataFrame:")
print(dataFrame.head() )



# Convertir de pandas a numpy
datos = pd.DataFrame(dataFrame).to_numpy()

print("saca las columnas de la matriz A")
matriz_a = datos[:,0:8]

print("saca la columna de la matriz B o el vector b")
matriz_b = datos[:,8]

print("verificacion....")
print(matriz_a[1,:])
print(matriz_b[1])

print("genera la pseudo inversa")

inv_matriz_a = np.linalg.pinv(matriz_a)

print("procede a la multiplicacion para ver los pesos del vector x")
pesos_x = np.matmul(inv_matriz_a, matriz_b)

print(pesos_x)

print(matriz_a[1,:])

eval = matriz_a[1,:]
pesos_x_t = np.transpose(pesos_x)
b_estimado = np.matmul(matriz_a, pesos_x_t)

punto_b = matriz_b[0:2]
punto_b_estimado =b_estimado[0:2]

print("-"*40)

print(" Valor definido ",punto_b)
print("-"*40)
print(" Valor estimado ", punto_b_estimado)
print("-"*40)
print("-"*40)
# Establece la base del origen de cada vector
x = np.array([0.,0.] )
y = np.array([0.,0.] )

fig, ax = plt.subplots()

ax.quiver(x, y, punto_b, punto_b_estimado ,color=["r","b"],angles='xy', scale_units='xy', scale=1)

ax.axis([-0.5,1.,-0.5,1.])
ax.set_aspect('equal')
plt.show()

print("fin")
