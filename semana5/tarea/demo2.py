import os

import pandas as pd
import numpy as np
#import sklearn.datasets
import matplotlib.pyplot as plt


ruta = os.getcwd()

print("x"*40)
print(ruta)
#plt.rcParams['figure.figsize'] = [8, 4]
ruta = ruta+"/semana5/tarea"

df = pd.read_csv(ruta+'/data_banknote_authentication.csv',sep=";")

print(df.shape)
df2 = df.iloc[:,:-1]

# escalar los datos X
df2_zscaled = (df2 - df2.mean()) / df2.std(ddof=1)
print(df2_zscaled[0:3])
# Saco el valor Y 
b = df.iloc[:,-1]


#etiquetado de cada clase
bb = b.apply(lambda cla: 'class1' if cla == 0 else 'class2' )
print(bb.shape)
#unir los dos dataframes
b_combinado = pd.concat([b, bb], axis=1)
b_combinado.columns = ['clases','descripcion']
print(b_combinado.shape)
print(df2_zscaled.shape)
print("x"*50)
print(b_combinado['descripcion'])

tiposClases = np.unique(b_combinado['descripcion'] )
print("tipos de clases " , tiposClases)

print(df2_zscaled.head(7))
# calcula los auto-valores y auto-vectores
eigenvalues, eigenvectors = np.linalg.eig( np.cov(df2_zscaled,rowvar=False))
print(eigenvalues)
# los normaliza
eigenvalues_normalized = eigenvalues / eigenvalues.sum()
print(eigenvalues_normalized)
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
print(proyeccion_data.head(5))
# agrega la etiqueta de las especies
proyeccion_data = pd.concat([proyeccion_data, b_combinado], axis=1)

print("Parte de las muestras proyectadas")
print(proyeccion_data.head(5))


las_clases = [proyeccion_data[proyeccion_data.clases=='Class1'], 
          proyeccion_data[proyeccion_data.clases=='Class2']]
print(las_clases)

# define un color por clase
colors = ['#1b9e77', '#d95f02', '#7570b3'] 
_, (ax1, ax2) = plt.subplots(1, 2, sharey=False)

# muestra el componente principal respecto al total de varianza en los datos
ax1.plot([1,2,3,4],
         eigenvalues_normalized,
         '-o',
         color='#8da0cb',
         label='auto-valor (normalizado)',
         alpha=0.8,
         zorder=1000)

ax1.plot([1,2,3,4],
         cumvar_explained,
         '-o',
         color='#fc8d62',
         label='varianza explicada',
         alpha=0.8,
         zorder=1000)

ax1.set_xlim(0.8, 4.2)
ax1.set_xticks([1,2,3,4])
ax1.set_xlabel('PCA')
ax1.set_ylabel('Varianza')
ax1.legend(loc='center right', fontsize=7)
ax1.grid(color='#fdfefe')
ax1.set_facecolor('#f4f6f7')

for group, color in zip(las_clases, colors):
    ax2.scatter(group.pc1,
                group.pc2,
                marker='^',
                color=color,
                label=group.clases,
                alpha=0.5,
                zorder=1000)
ax2.set_xlabel(r'PC-1')
ax2.set_ylabel(r'PC-2')
ax2.grid(color='#fdfefe')
ax2.set_facecolor('#f4f6f7')
ax2.legend(labels=tiposClases, fontsize=7)

ax3 = ax2.twinx()
for group, color in zip(las_clases, colors):
    ax3.scatter(group.pc1,
                group.pc3,
                marker='^',
                color=color,
                label=group.descripcion,
                alpha=0.5,
                zorder=1000)
ax3.set_ylabel(r'PC-3')


plt.suptitle(r'Visualización del PCA via auto-valores y auto-vectores, 2D')
plt.tight_layout(pad=3.0)
plt.show()    

print()
#print(df.to_string()) 