import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución binomial
n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito
tamaño_muestra = 1000

# Generar una muestra aleatoria de la distribución binomial
muestra = np.random.binomial(n, p, tamaño_muestra)

# Crear el histograma de frecuencias
plt.hist(muestra, bins=np.arange(n+2)-0.5, rwidth=0.8, alpha=0.7)

# Configurar el gráfico
plt.xlabel('Número de éxitos')
plt.ylabel('Frecuencia')
plt.title('Distribución de probabilidad binomial')
plt.xticks(range(n+1))
plt.grid(True)

# Mostrar el gráfico
plt.show()