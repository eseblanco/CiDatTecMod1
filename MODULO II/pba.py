

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# Generar datos simulados
np.random.seed(42) # Para reproducibilidad
data = {
    'Edad': np.random.randint(20, 60, 100),
    'Ingresos': np.random.normal(50000, 15000, 100),
    'Años_Experiencia': np.random.randint(1, 20, 100),
    'Ciudad': np.random.choice(['A', 'B', 'C', 'D'], 100, p=[0.4, 0.3, 0.2, 0.1]),
}
df = pd.DataFrame(data)

# Añadir un valor atípico (outlier) para ilustrar
df.loc[99, 'Ingresos'] = 250000 

print("Primeras filas del DataFrame:")
print(df.head())
print("\nResumen Estadístico:")
print(df.describe())

# Configuración de la figura para dos gráficos
plt.figure(figsize=(15, 5))

# --- Histograma de Ingresos ---
plt.subplot(1, 2, 1) # 1 fila, 2 columnas, posición 1
plt.hist(df['Ingresos'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribución de Ingresos')
plt.xlabel('Ingresos ($)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.5)

# --- Box Plot (Diagrama de Caja) de Ingresos ---
plt.subplot(1, 2, 2) # 1 fila, 2 columnas, posición 2
plt.boxplot(df['Ingresos'], vert=False, patch_artist=True, 
            boxprops=dict(facecolor='lightgreen', color='black'))
plt.title('Box Plot de Ingresos')
plt.xlabel('Ingresos ($)')
plt.yticks([1], ['Ingresos'])
plt.grid(axis='x', alpha=0.5)

plt.tight_layout() # Ajustar el espacio entre gráficos
plt.show()