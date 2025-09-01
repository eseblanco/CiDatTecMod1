import numpy as np
# Descenso de gradiente
# Función:  f( x, y ) =  x^2 - y^2
# código base: https://towardsdatascience.com/implement-gradient-descent-in-python-9b93ed7108d1

def gradiente_fxy(x, y):
    # derivadas parciales
    # deriv f / x = 2x
    # deriv f / y = -2y
    return np.array([2*x, -2*y])

#def SGD(tasa_aprendizaje, iteraciones, xy, tolerancia) -> None:
tasa_aprendizaje=0.25
iteraciones=1000
cur_xy=np.array((100, 0), dtype=float) # son los valores iniciales de X , Y 
tolerancia=0.000000000000000000000000001
previous_step_size = 1
iters = 0 #iteration counter
print("Initial point : ", cur_xy)
while previous_step_size > tolerancia and iters < iteraciones:
   prev_xy = cur_xy # Store current point value in previous_point
   cur_xy = prev_xy - tasa_aprendizaje * gradiente_fxy(prev_xy[0], prev_xy[1]) #Grad descent
   previous_step_size = np.linalg.norm(cur_xy - prev_xy, ord=2) # Euclidean distance
   iters += 1 #iteration count
   if (iters % 1) == 0:
      print("Iteration",iters,"\nPoint value is", cur_xy) #Print iterations
      print("previous_step_size >>> ", previous_step_size)


print("The local minimum occurs at", cur_xy)

