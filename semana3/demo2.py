import numpy as np
import pandas as pd


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

print("fin")