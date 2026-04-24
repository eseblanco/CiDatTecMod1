from ucimlrepo import fetch_ucirepo
  
# obtener conjunto de datos
marketing_banco = fetch_ucirepo(id=222)
  
# datos (como dataframes de pandas)
X = características_de_datos_de_marketing_bancario
y = datos_objetivos_marketing_bancario
  
# metadatos
imprimir(marketing_banco.metadatos)
  
# información variable
imprimir(variables_marketing_banco)