import numpy as np

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
        # el siguiente IF lo que realiza es que verifica que la norma del vector sea mayor que 0 
        # para asegurarse que no tener error en la normalización. 
        if np.isclose(np.linalg.norm(tmp_a[:, j]), 0, rtol=1e-15, atol=1e-14, equal_nan=False):
            tmp_a[:, j] = np.zeros(tmp_a.shape[0])
        else:    
            print(np.linalg.norm(tmp_a[:, j]))
            tmp_a[:, j] = tmp_a[:, j] / np.linalg.norm(tmp_a[:, j])
    return tmp_a

# Ejemplo de uso
a = np.array([
    [16.0, 25.0, 99.0],
    [22.0, 44.0, 24.0],
    [0.0, 2.0, 18.0]
])
print("="*50)
print(np.dot(a[:, 0], a[:, 1]) * a[:, 0])
print(np.linalg.norm(a[:, 1]))

q = gram_schmidt_orthonormal(a)

print("Matriz ortonormal:")
print(q)
print("-"*40)
q_t = np.transpose(q)  # se puede usar  q.T  lo cue devuelve de una vez la tarnspuesta 

q1_result = np.matmul(q.T,q) 
q1_result = q.T@q   # se puede utilizar el @ en vez de matmul ya que esta sobrecargado en la misma biblioteca. 

print(q1_result)
print("-"*40)

q2_result  = q@q.T
print("-"*40)
print("sin redondeo******")
print(q2_result)
print("-"*40)
print(np.round(q2_result,8))




a = np.array([
    [1.0, -1.0, 0.0],
    [1.0, 2.0, 1.0],
    [0.0, 1.0, 1.0]
])
