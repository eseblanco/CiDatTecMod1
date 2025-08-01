import numpy as np
import pandas as pd

separador = "-"*40
archivo = "/home/sblanco/Documentos/PycharmProjects/CienciaDatosTEC/tarea-semana2/Datos_01.csv"

# carga el archivo en pandas
#/home/sblanco/Documentos/PycharmProjects/CienciaDatosTEC/tarea-semana2/demo.py
dataFrame = pd.read_csv(archivo, header = 0, delimiter=';')

# guarda el nombre de las columnas en una lista
colNames = dataFrame.columns

# muestra los primeros elementos del dataFrame
print(separador)
print("Datos en dataFrame:")
print(dataFrame.head() )

# Convertir de pandas a numpy
datos = pd.DataFrame(dataFrame).to_numpy()


# En cada vector columna hay un atributo
# El atributo1 está en datos[:,0]
# El atributo2 está en datos[:,1]
# y así sucesivamente

columns = datos.shape[1]

for i in range(0,columns):
    for j in range(columns-1,-1,-1):
        if i != j:
          alpha = datos[0,i] / datos[0,j]
          vector = alpha * datos[:,j]
          eval_vec = datos[:,i]
          if np.array_equal(eval_vec , vector):
            print(f"Columna {i} es colineal de la columna {j}")
            
