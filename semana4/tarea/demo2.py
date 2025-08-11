import numpy as np

def proyectar_Matriz(y, A):
  """
  y: column vector, 2d array
  A: n x m matrix, 2d array
  """
  invMatrix = np.linalg.pinv(a.T@a)
  u_result = ((a @ invMatrix) @ q.T) @ u
  invMatrix = np.linalg.pinv(np.matmul(a.T,a))
  return np.matmul( np.matmul(np.matmul(a,invMatrix), a.T), u)
  return u_result


def proyectar_Matriz2(y, A):
  """
  y: column vector, 2d array
  A: n x m matrix, 2d array
  """
  
  a1 = A@A.T 
  a2 = A.T@A
  
  a3 = a1/a2
  a4 = a3@y
  return a4




def error_Proyeccion(v, y):
  """
  Calcualte projection error by using the euclidian distance
  """
  return np.linalg.norm(v - y, 2)


def gram_schmidt_orthonormal(mat):
    """
    Aplica el proceso de Gram-Schmidt para obtener una base ortonormal
    a partir de una matriz cuyas columnas son vectores.
    """
    tmp_a = np.copy(mat).astype(np.float64) # Se crea una instacia local 
    n = tmp_a.shape[1]
    for j in range(n):
        # Para cada vector en las Columna j se debe encontrar la proyección perpendicular
        # de los vectores ortogonales previos.
        for k in range(j):
            tmp_a[:, j] -= np.dot(tmp_a[:, k], tmp_a[:, j]) * tmp_a[:, k]
        # 
        # Normalizar la matriz
        # el siguiente IF, lo que realiza es que verifica que la norma del vector sea mayor que 0 
        # para asegurarse que no tener error en la normalización. 
        if np.isclose(np.linalg.norm(tmp_a[:, j]), 0, rtol=1e-15, atol=1e-14, equal_nan=False):
            tmp_a[:, j] = np.zeros(tmp_a.shape[0])
        else:    
            tmp_a[:, j] = tmp_a[:, j] / np.linalg.norm(tmp_a[:, j])
    return tmp_a

# Ejemplo de uso
a = np.array([
    [16.0, 0.30, 99.0],
    [22.0, 44.0, 24.0],
    [0.0, 2.033, 18.780]
])

q = gram_schmidt_orthonormal(a)
q=a
print("Matriz Original:")
print(a)
print("-"*40)

print("Matriz ortonormal:")
print(q)
print(q@q.T)

print("m"*40)
q_t = np.transpose(q)  # se puede usar  q.T  el cual devuelve de una vez la tarnspuesta 

q1_result = q.T@q   # se puede utilizar el @ en vez de matmul ya que esta 
                    # sobrecarga del operador esta en la misma biblioteca. 


print()
print()
print()

print("."*40)
print("x"*40)

print()
print()
print()

print(a)
print("="*40)

# Vector de ejempo
u = np.array    ([[43.0],
                  [232.0],
                  [453]])
#u = np.array    ([[4334.0,232.0,453]])
#u = np.array    ([[4334.0], [232.0],[453]])
print(u)
print(q.shape , " --- ", u.shape)

print("X"*40)

ojas = np.matmul( np.matmul(np.matmul(q,np.linalg.pinv(np.matmul(q.T,q))), q.T), u)

print( ojas)

print("-"*40)

print("-"*40)
bb=proyectar_Matriz2(u,a)
print(bb)
print("-"*40)

print(error_Proyeccion(u, bb))
print("-"*40)
#u_result2 = q @ q.T * u
#print (u_result2)
#print("-"*40)