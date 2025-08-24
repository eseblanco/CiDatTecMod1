from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

ruta="/home/sblanco/Documentos/PycharmProjects/CienciaDatosTEC/semana6/tarea"


plt.style.use('ggplot')
img = Image.open(ruta+'/Perrita.jpg')

print("Detalles de img: ", img)
# convertir imagen a "true color"

img_array = np.array(img,float)

plt.figure(figsize=(9, 6))
plt.imshow(img)
plt.show() 

 #print("Detalles de imggray: ", imggray)
 # sacar cada matriz. 


rojo_matriz = img_array[:, :, 0]
verde_matriz = img_array[:, :, 1]
azul_matriz = img_array[:, :, 2]
# convert to numpy array
# Reshape according to orginal image dimensions
print("\nMatriz original:")
print(img_array.shape)
print("\nMatriz del canal rojo:")
print(rojo_matriz.shape)
print("\nMatriz del canal verde:")
print(verde_matriz.shape)
print("\nMatriz del canal azul:")
print(azul_matriz.shape)

# aplico SVD a cada matriz
U_azul, D_azul, V_azul = np.linalg.svd(azul_matriz)

U_rojo, D_rojo, V_rojo = np.linalg.svd(rojo_matriz)

U_verde, D_verde, V_verde = np.linalg.svd(verde_matriz)


for i in [5, 10, 50, 100, 300, 700]:
    #reconstimg = np.matrix(U[:, :i]) * np.diag(D[:i]) * np.matrix(V[:i, :])
    azul_matriz = np.matmul( np.matmul( np.matrix(U_azul[:, :i]) , np.diag(D_azul[:i]) ) , np.matrix(V_azul[:i, :]) )
    rojo_matriz = np.matmul( np.matmul( np.matrix(U_rojo[:, :i]) , np.diag(D_rojo[:i]) ) , np.matrix(V_rojo[:i, :]) )
    verde_matriz = np.matmul( np.matmul( np.matrix(U_verde[:, :i]) , np.diag(D_verde[:i]) ) , np.matrix(V_verde[:i, :]) )
    altura, anchura = azul_matriz.shape
    arreglo_combinado = np.zeros((altura, anchura, 3), dtype=np.uint8)
    arreglo_combinado[:, :, 0] = rojo_matriz
    arreglo_combinado[:, :, 1] = verde_matriz
    arreglo_combinado[:, :, 2] = azul_matriz

    print(arreglo_combinado.shape)

    # Convertir el array de NumPy de vuelta a un objeto de imagen de Pillow
    imagen_combinada = Image.fromarray(arreglo_combinado, 'RGB')
    plt.imshow(imagen_combinada)
    title = "n = %s" % i
    plt.title(title)
    plt.show()