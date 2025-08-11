import numpy as np
from numpy import linalg as LA

def projectInvertible(y, A):
  """
  y: column vector, 2d array
  A: n x m matrix, 2d array
  """
  At = np.transpose(A)
  invMatrix = LA.inv(np.matmul(At,A))
  print(invMatrix)
  
  print(np.matmul( 
                  np.matmul(
                    np.matmul(A,invMatrix),
                    At), 
                  y))
  
  
  return np.matmul( np.matmul(np.matmul(A,invMatrix), At), y)

def calculateProjectionError(v, y):
  """
  Calcualte projection error by using the euclidian distance
  """
  return LA.norm(v - y, 2)

y = np.array    ([[766.0],
                  [10.0],
                  [3.7826]])

A = np.array    ([ [0.5, 0,    0],
                   [0,   0.25, 0],
                   [0,   0,    2]])
#calculate the projection
projY_A = projectInvertible(y,A)
print("Vector proyectado: ")
print(projY_A)
#calculate its error, which should be zero for invertible A, or lineally independent base vectors
print("Error de proyección: ")
error = calculateProjectionError(projY_A, y)
print(error)

