
import numpy as np
import matplotlib.pyplot as plt
import kagglehub
#import zipfile
import numpy as np
import pandas as pd
import seaborn as sms

#%matplotlib inline

#https://www.kaggle.com/datasets/diegorojasdiaz/123-emergency-calls-in-bogota
# Download latest version
#path = kagglehub.dataset_download("diegorojasdiaz/123-emergency-calls-in-bogota")
path = "/home/sblanco/.cache/kagglehub/datasets/diegorojasdiaz/123-emergency-calls-in-bogota/versions/4"
print("\n Path to dataset files:\n\n", path)

emergencia_data = pd.read_csv(path+"/clean_df_123.csv")

print(emergencia_data.head())

print("\n\n Informacion del DataFrame:\n")

print(emergencia_data.info())






emergencia_data['GENERO'].replace(['', ' '], np.nan, inplace=True) 

# 2. Contar las ocurrencias de cada valor único en 'GENERO'
gender_counts = emergencia_data['GENERO'].value_counts()

# 3. Generar el gráfico de barras
plt.figure(figsize=(8, 6))

bars = plt.bar(
    gender_counts.index, 
    gender_counts.values, 
    color=['skyblue', 'salmon', 'lightgreen'], 
    edgecolor='black'
)

plt.title('Distribución de Llamadas por GÉNERO', fontsize=16)
plt.xlabel('GÉNERO', fontsize=12)
plt.ylabel('Frecuencia (Cantidad de Llamadas)', fontsize=12)
plt.grid(axis='y', alpha=0.5)

# Añadir etiquetas de conteo
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 500, int(yval), ha='center', va='bottom')

plt.tight_layout()
plt.savefig('gender_distribution_bar_chart.png')
plt.show()