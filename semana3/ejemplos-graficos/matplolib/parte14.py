"""
es un diagrama de caja-bigote
REVISAR

"""
import matplotlib.pyplot as plt
import numpy as np

alt_esp = np.random.randn(100)+165 + np.random.randn(100) * 10
# Creamos unos valores para la altura de 100 españolas

alt_ale = np.random.randn(100)+172 + np.random.randn(100) * 12
# Creamos unos valores para la altura de 100 alemanas

alt_tai = np.random.randn(100)+159 + np.random.randn(100) * 9
# Creamos unos valores para la altura de 100 tailandesas

plt.boxplot([alt_esp, alt_ale, alt_tai], sym = 'ko', whis = 1.5)
# El valor por defecto para los bigotes es 1.5*IQR pero lo escribimos
# explícitamente

plt.xticks([1,2,3], ['Esp', 'Ale', 'Tai'], size = 'small', color = 'k')
# Colocamos las etiquetas para cada distribución

plt.ylabel(u'Altura (cm)')

plt.show()