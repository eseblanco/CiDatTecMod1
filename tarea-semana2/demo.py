import numpy as np
import pandas as pd


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


for i in range(0,columns1):
    vector3.append(vector2[i] * factor)
    
if vector1 == vector3 : 
    print("colineales")
else:
    print("no colineales")    