"""
revisar mas

"""
import matplotlib.pyplot as plt
import numpy as np

s1x = [0.3,0.3,0.7,0.7,0.5,0.5,1,1,0.7,0.7]
s1y = [0.5,1.4,1.4,1.5,1.5,1.9,1.9,1.1,1.1,0.5]
o1x = [0.6,0.6,0.7,0.7]
o1y = [1.7,1.8,1.8,1.7]
s2x = [0.8,0.8,1.1,1.1,1.5,1.5,1.1,1.1,1.3,1.3]
s2y = [0.2,1,1,1.6,1.6,0.7,0.7,0.6,0.6,0.2]
o2x = [1.1,1.1,1.2,1.2]
o2y = [0.3,0.4,0.4,0.3]
plt.fill(s1x, s1y, color = 'b')
plt.fill(o1x,o1y, color = 'w')
plt.fill(s2x, s2y, color = 'g')
plt.fill(o2x,o2y, color = 'w')
plt.title(u'Símbolo de python cutre')
plt.ylim(0.1,2)

plt.show()