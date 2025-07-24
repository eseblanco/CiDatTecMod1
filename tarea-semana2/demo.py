
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import math

vector1 = [1,2,3]
vector2 = [10,20,30]
vector3 = []
columns1 = len(vector1)
columns2 = len(vector2)
factor = vector1[0] / vector2[0]


for i in range(0,columns1):
    vector3.append(vector2[i] * factor)
    
if vector1 == vector3 : 
    print("colineales")
else:
    print("no colineales")
    
    
    
    
vector1 = [10,20,30,20,10,11]

vector3 = []
columns1 = len(vector1)
columns2 = len(vector2)
factor = vector1[0] / vector2[0]

"""
for i in range(0,columns1):
    vector3.append(vector2[i] * factor)
    
if vector1 == vector3 : 
    print("colineales")
else:
    print("no colineales")    
    

"""

vector1 = [1,2]
vector2 = [10,20]

vector1 = np.array([1.,2.] )
vector2 = np.array([10.,20.] )

fig, ax = plt.subplots()
ax.quiver(vector1, vector2,color=["r","b"],angles='xy', scale_units='xy', scale=1)
ax.axis([-3.,20.,-3.,23.])
ax.set_aspect('equal')
plt.show()


vector3 = []
columns1 = len(vector1)
columns2 = len(vector2)
factor = vector1[0] / vector2[0]


for i in range(0,columns1):
    vector3.append(vector2[i] * factor)

vector3 = np.array(vector3 )
#vector3 = np.array( vector3 )
if np.array_equal(vector1 ,vector3): 
    display(Markdown("## Respuesta :"))
    print("--->   Son colineales")
else:
    display(Markdown("## Respuesta :"))
    print("--->   No son colineales")