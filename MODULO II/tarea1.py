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


# Contar la cantidad de valores NaN en la columna 'EDAD'
emergencia_data['EDAD'] = pd.to_numeric(emergencia_data['EDAD'], errors='coerce')
nan_count = emergencia_data['EDAD'].isna().sum()
print(f"Cantidad total de lineas ': {len(emergencia_data)}  \n")
print(f"Cantidad de valores NaN en la columna 'EDAD': {nan_count}  \n")
print(f"Cantidad de valores en la columna 'EDAD': {len(emergencia_data) - nan_count}  \n")
print(f"Porcentaje de valores en la columna 'EDAD': { nan_count / len(emergencia_data) *100 }  \n")
print(f"Valor maximo es {emergencia_data['EDAD'].max()} \n")
print(f"Valor mínimo es {emergencia_data['EDAD'].min()} \n ")
print(f"Media de la EDAD  {emergencia_data['EDAD'].mean()} \n")
print(f"Mediana de la EDAD {emergencia_data['EDAD'].median()} \n")
print(f"Moda de la EDAD {emergencia_data['EDAD'].mode()[0]} \n")
print(f"Desviación estándar de la EDAD {emergencia_data['EDAD'].std()} \n")
print(f"Varianza de la EDAD {emergencia_data['EDAD'].var()} \n")
print(f"Rango de la EDAD {emergencia_data['EDAD'].max() - emergencia_data['EDAD'].min()} \n")
print(f"Percentil 25 de la EDAD {emergencia_data['EDAD'].quantile(0.25)} \n")
print(f"Percentil 75 de la EDAD {emergencia_data['EDAD'].quantile(0.75)} \n")
print(f"Coeficiente de variación de la EDAD {emergencia_data['EDAD'].std() / emergencia_data['EDAD'].mean()} \n")
print(f"Kurtosis de la EDAD {emergencia_data['EDAD'].kurtosis()} \n")
print(f"Asimetría de la EDAD {emergencia_data['EDAD'].skew()} \n")


# 2. Agrupar por 'TIPO_INCIDENTE' y calcular la edad máxima (.max() ignora NaN)
mediana_edad_por_accidente = emergencia_data.groupby('TIPO_INCIDENTE')['EDAD'].median()

#.sort_values(ascending=False)
cantidad_por_accidente = emergencia_data.groupby('TIPO_INCIDENTE')['EDAD'].count()
#.sort_values(ascending=False)
# 3. Mostrar el resultado completo
print("--- Edades Máximas por Tipo de Incidente (Ordenadas de Mayor a Menor) ---")
print(mediana_edad_por_accidente.to_string())
print("\n--- Cantidad de Registros por Tipo de Incidente (Ordenadas de Mayor a Menor) ---")
print(cantidad_por_accidente.to_string())


#print("--- Resultados Combinados: Tipo de Incidente, Edad Mediana y Cantidad de Registros ---")
#print(resultados_combinados.to_string(index=False))


emergencia_data['EDAD'] = pd.to_numeric(emergencia_data['EDAD'], errors='coerce')

# 2. Filtrar el DataFrame: Solo filas donde EDAD es NaN
registros_nan_edad = emergencia_data[emergencia_data['EDAD'].isna()]

# 3. Contar la frecuencia de los TIPO_INCIDENTE en este subconjunto
conteo_nan_por_incidente = registros_nan_edad['TIPO_INCIDENTE'].value_counts()

resultados_combinados = pd.DataFrame({
    'Edad Mediana': mediana_edad_por_accidente,
    'Cantidad de Registros': cantidad_por_accidente,
    'valores NaN en EDAD': conteo_nan_por_incidente
}).reset_index() 

resultados_combinados_ordenados = resultados_combinados.sort_values(
    by='Edad Mediana', 
    ascending=False
)


print(resultados_combinados_ordenados.to_string(index=False))


"""
def get_first_mode(series):
    # Filtrar NaNs
    cleaned_series = series.dropna()
    if cleaned_series.empty:
        return np.nan
    # Devolver el valor más frecuente (Moda). Se toma [0] por si hay múltiples modas.
    return cleaned_series.mode().iloc[0]

# 3. Aplicar la función a cada grupo de 'TIPO_INCIDENTE'
most_frequent_age_per_incident = emergencia_data.groupby('TIPO_INCIDENTE')['EDAD'].apply(get_first_mode).sort_values(ascending=False)

# 4. Mostrar el resultado
print("Edad más Frecuente (Moda) por Tipo de Incidente:")
print(most_frequent_age_per_incident.to_string())

# Mostrar la moda general
overall_mode_age = df['EDAD'].dropna().mode().iloc[0]
print(f"\nLa edad más frecuente en todo el dataset es: {int(overall_mode_age)} años.")



fig, (ax_hist, ax_box) = plt.subplots(
    2, 1, 
    sharex=True, 
    figsize=(10, 6),
    gridspec_kw={'height_ratios': [4, 1]} # Proporción de alturas [4 (hist), 1 (box)]
)

# 2. Eliminar el espacio vertical entre los subplots
fig.subplots_adjust(hspace=0)

# --- Histograma de EDAD (Superior) ---
# Se utiliza ax_hist para el histograma
ax_hist.hist(
    emergencia_data['EDAD'].dropna(), 
    bins=15, 
    color='skyblue', 
    edgecolor='black'
)
ax_hist.set_title('Distribución de EDAD y Diagrama de Caja', fontsize=14)
ax_hist.set_ylabel('Frecuencia', fontsize=12)
ax_hist.grid(axis='y', alpha=0.5)

# Ocultar las etiquetas del eje X en el histograma para evitar redundancia
ax_hist.tick_params(axis="x", labelbottom=False)

# --- Box Plot (Diagrama de Caja) de EDAD (Inferior) ---
# Se utiliza ax_box para el box plot
ax_box.boxplot(
    emergencia_data['EDAD'].dropna(), 
    vert=False, # Horizontal
    patch_artist=True, 
    boxprops=dict(facecolor='lightgreen', color='black'),
    flierprops=dict(marker='o', markersize=5, markerfacecolor='red', alpha=0.5) # Estilo de Outliers
)
ax_box.set_xlabel('EDAD (años)', fontsize=12)
ax_box.set_yticks([]) # Eliminar la etiqueta de Y para el box plot
ax_box.grid(axis='x', alpha=0.5)

plt.show()






"""