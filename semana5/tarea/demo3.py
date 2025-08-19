import os

import pandas as pd
import numpy as np
#import sklearn.datasets
import matplotlib.pyplot as plt
import plotly.express as px

ruta = os.getcwd()

print("x"*40)
print(ruta)
#plt.rcParams['figure.figsize'] = [8, 4]
ruta = ruta+"/semana5/tarea"

df = pd.read_csv(ruta+'/data_banknote_authentication.csv',sep=";")

print(df.shape)
df2 = df.iloc[:,:-1]

#print(b.shape)
#print(df2.shape)


# Escalar los datos en df2
df2_zscaled = (df2 - df2.mean()) / df2.std(ddof=1)

b = df.iloc[:,-1]
#etiquetado de cada clase
bb = b.apply(lambda cla: 'class1' if cla == 0 else 'class2' )
print(bb.shape)
#unir los dos dataframes
b_combinado = pd.concat([b, bb], axis=1)
b_combinado.columns = ['clases','descripcion']
print(b_combinado.shape)
print("x"*50)
print(b_combinado['descripcion'])
# calcula los auto-valores y auto-vectores

tiposClases = np.unique(b_combinado['descripcion'] )
print("tipos de clases " , tiposClases)


# calcula los auto-valores y auto-vectores
eigenvalues, eigenvectors = np.linalg.eig( np.cov(df2_zscaled,rowvar=False))

# los normaliza
eigenvalues_normalized = eigenvalues / eigenvalues.sum()
# calcula la varianza explicada
cumvar_explained = np.cumsum(eigenvalues_normalized)

############################################################
# Ordenar de mayor a menor, 
# debido a que np.linalg.eig no asegura que vengan ordenados
idx = np.argsort(eigenvalues) 
print( "idx: ", idx )
idx = idx[::-1]     
print("\n\nidx[::-1]: ", idx  )


# Ordenar tanto los autovalroes como los autovectores
eigenvectors = eigenvectors[:,idx]
eigenvalues = eigenvalues[idx] 

print("Auto-valores:")
print(eigenvalues)
print("Auto-vectores:")
print( eigenvectors)
print("eigenvalues_normalized:")
print(eigenvalues_normalized)
print("Varianza explicada:")
print( cumvar_explained )

proyeccion_data = pd.DataFrame(df2_zscaled.dot(eigenvectors))

# Nombres de columnas
proyeccion_data.columns = ['pc1', 'pc2', 'pc3', 'pc4']

# agrega la etiqueta de las especies
proyeccion_data = pd.concat([proyeccion_data, b_combinado], axis=1)

print("Parte de las muestras proyectadas")
print(proyeccion_data.head(5))


las_clases = [proyeccion_data[proyeccion_data.clases=='Class1'], 
          proyeccion_data[proyeccion_data.clases=='Class2']]
print(las_clases)


fig = px.scatter_3d(proyeccion_data, x='pc1', y='pc2', z='pc3',
              color='class')
fig.show()



print()
#print(df.to_string()) 