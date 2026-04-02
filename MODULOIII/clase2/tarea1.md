# Documentación de Razonamiento - Tarea 1 Parte 1

Este documento detalla el razonamiento matemático y lógico utilizado para resolver los ejercicios de la Parte 1.

## Ejercicio 1: Análisis de Ventas de Bienes Raíces

El objetivo de este ejercicio es aplicar conceptos básicos de probabilidad utilizando una tabla de contingencia que resume datos históricos de ventas.

### 1. Estimación de Probabilidades Simples ($P(A)$ y $P(B)$)
Para estimar la probabilidad de un evento simple, utilizamos el enfoque frecuentista (definición de Laplace). Asumimos que la frecuencia relativa observada en los datos es una buena estimación de la probabilidad real.

*   **Fórmula:** $P(E) = \frac{\text{Número de casos favorables al evento E}}{\text{Número total de casos}}$
*   **Razonamiento:**
    *   Para $P(A)$ (venta > 90 días), sumamos todas las ventas en la columna "Más de 90" y dividimos por el gran total.
    *   Para $P(B)$ (precio < $50k), sumamos todas las ventas en la fila "Menos de $50,000" y dividimos por el gran total.

### 2. Probabilidad Conjunta ($P(A \cap B)$)
La probabilidad conjunta representa la probabilidad de que dos eventos ocurran simultáneamente.

*   **Razonamiento:** Identificamos la celda en la tabla donde se cruzan la fila de $B$ (Menos de $50,000) y la columna de $A$ (Más de 90 días). El valor en esta celda representa la intersección. Dividimos este valor por el gran total.

### 3. Probabilidad Condicional ($P(A^c | B)$)
La probabilidad condicional $P(E|F)$ mide la probabilidad de $E$ dado que ya sabemos que $F$ ha ocurrido. Esto reduce nuestro espacio muestral de "toda la población" a solo "los casos donde ocurre F".

*   **Definición:** El evento "tarde 90 o menos días" es el complemento de $A$, denotado como $A^c$.
*   **Fórmula:** $P(A^c | B) = \frac{P(A^c \cap B)}{P(B)} = \frac{\text{Casos en } A^c \cap B}{\text{Total de casos en } B}$
*   **Razonamiento:** Nos restringimos únicamente a la fila de "Menos de $50,000" (Total = 100). Dentro de ese subgrupo, contamos cuántos tardaron 90 días o menos (suma de "Menos de 30" y "De 31 a 90"). La razón entre estos dos números es la probabilidad condicional.

### 4. Independencia de Eventos
Dos eventos son estadísticamente independientes si la ocurrencia de uno no afecta la probabilidad de ocurrencia del otro.

*   **Condición Matemática:** $A$ y $B$ son independientes si y solo si $P(A \cap B) = P(A) \cdot P(B)$.
*   **Razonamiento:**
    1.  Tomamos el valor calculado de $P(A \cap B)$.
    2.  Calculamos el producto de las probabilidades marginales $P(A) \cdot P(B)$.
    3.  Comparamos ambos valores. Si son diferentes (como resultó ser el caso), concluimos que existe una dependencia entre el precio de la casa y el tiempo que tarda en venderse.

---

## Ejercicio 2: Análisis de Variables Aleatorias

Este ejercicio se centra en la estadística descriptiva multivariada para muestras pequeñas ($N=3$).

### 1. Cálculo de la Varianza ($s^2$)
La varianza mide la dispersión de los datos respecto a su media. Dado que estamos trabajando con una muestra (no la población entera), utilizamos la varianza muestral.

*   **Fórmula:** $s^2 = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2$
*   **Pasos:**
    1.  **Media ($\bar{x}$):** Sumamos los valores y dividimos entre $N=3$.
    2.  **Desviaciones:** Restamos la media a cada valor individual.
    3.  **Cuadrados:** Elevamos al cuadrado cada desviación (esto elimina signos negativos y penaliza más los valores lejanos).
    4.  **Suma:** Sumamos los cuadrados.
    5.  **Promedio corregido:** Dividimos entre $N-1$ (grados de libertad) para obtener un estimador insesgado.

### 2. Matriz de Correlación de Pearson ($R$)
El coeficiente de correlación de Pearson ($r$) mide la fuerza y dirección de la relación lineal entre dos variables.

*   **Fórmula:** $r_{xy} = \frac{Cov(x,y)}{s_x \cdot s_y}$
*   **Componentes:**
    *   **Covarianza ($Cov(x,y)$):** Mide cómo varían dos variables juntas.
        *   $Cov(x,y) = \frac{1}{N-1} \sum (x_i - \bar{x})(y_i - \bar{y})$
    *   **Desviación Estándar ($s$):** Es la raíz cuadrada de la varianza ($s = \sqrt{s^2}$). Sirve para normalizar la covarianza.
*   **Razonamiento:**
    1.  Calculamos la covarianza para cada par de variables ($h_1-h_2$, $h_1-h_3$, $h_2-h_3$).
    2.  Dividimos cada covarianza por el producto de las desviaciones estándar de las variables involucradas.
    3.  Organizamos los resultados en una matriz simétrica donde la diagonal principal es siempre 1 (correlación de una variable consigo misma).
