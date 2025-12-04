import numpy as np


# 1. Crear una funcion que genere puntos muestrales aleatorios dadas las dos probabilidades de manzana y
#naranja (como parametro)

#Definir las probabilidades a priori

prob_manzana_roja = 1/4
prob_naranja_roja = 3/4
prob_manzana_azul = 3/4
prob_naranja_azul = 1/4
prob_roja = 0.4
prob_azul= 0.6


def generar_observacion():
    caja = np.random.choice(['roja','azul'], p=[prob_roja,prob_azul])
    if caja == 'roja':
        fruta = np.random.choice(['manzana', 'naranja'], p=[prob_manzana_roja,prob_naranja_roja])
    else:
        fruta = np.random.choice(['manzana', 'naranja'], p=[prob_manzana_azul, prob_naranja_azul])
    return caja, fruta


# 2. Crear una función que genere muestras a partir del paso 1 (el tamaño de la caja se recibe por parametro) Cada caja es un conjunto de muestras

def generar_muestra(num_muestras, num_observaciones):
    muestras = []
    for i in range(num_muestras):
        muestras = [ generar_observacion() for _ in range(num_observaciones)]
        muestras.append(muestras)
    return muestras

# 3. Luego de generar 3 muestras de diferentes tamanios y con diferentes probabilidades 
# a priori. Cree funciones para calcular la probabilidad de obtener cualquier 
# fruta (evidencia) y la probabilidad a posteriori de
# cualquier caja dado que se escogió una fruta en particular

def calcular_probabilidad_fruta(muestras, fruta):
    return sum(1 for _, f in muestras if f == fruta) / len(muestras)

def calcular_probabilidad_caja(muestras, caja):
    return sum(1 for c, _ in muestras if c == caja) / len(muestras)

def calcular_probabilidad_posterior(muestras, fruta, caja):
    return calcular_probabilidad_fruta(muestras, fruta) * calcular_probabilidad_caja(muestras, caja)

def probabilidad_marginal(muestras, fruta):
    total_muestras = sum(len(muestra) for muestra in muestras)
    contador_muestra = sum(1 for muestra in muestras for _,m in muestra if m== fruta )
    return contador_muestra/total_muestras


if __name__ == '__main__':
    muestras = generar_muestra(10, 10)
    print(muestras)
    print(calcular_probabilidad_fruta(muestras, 'manzana'))
    print(calcular_probabilidad_caja(muestras, 'roja'))
    print(calcular_probabilidad_posterior(muestras, 'manzana', 'roja'))    
    prob_manzana = probabilidad_marginal(muestras, 'manzana')
    prob_naranja = probabilidad_marginal(muestras, 'naranja')
    print(f"Probabilidad marginal de manzana: {prob_manzana:.2f}")
    print(f"Probabilidad marginal de naranja: {prob_naranja:.2f}")    
