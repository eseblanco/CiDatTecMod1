import math
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

separador = "-"*40
archivo = "/home/sblanco/Documentos/PycharmProjects/CienciaDatosTEC/tarea-semana2/Datos_01.csv"

# carga el archivo en pandas
#/home/sblanco/Documentos/PycharmProjects/CienciaDatosTEC/tarea-semana2/demo.py
A = np.array([ [1. , 2. , 3. ], [4. , 5. , 6. ] , [7. , 8. , 91.]])
print( A )
print("ssssssssssssssssssssssssssssssssssssssss" )
T = np.transpose(A)
print( T )

print("ssssssssssssssssssssssssssssssssssssssss" )
print("ssssssssssssssssssssssssssssssssssssssss" )
# otro modo
A = np.array([ [1. , 2. , 3. ], [4. , 5. , 6. ] , [7. , 8. , 91.]])
T = A.transpose(1,0)
print(T)

print("ssssssssssssssssssssssssssssssssssssssss" )
print("ssssssssssssssssssssssssssssssssssssssss" )
T = A.transpose(0,1)
print(T)
