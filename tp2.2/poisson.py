import numpy as np
import matplotlib.pyplot as plt

# Parametro de la distribucion Poisson
lambda_param = 5  # Tasa media de ocurrencia
tamanio_muestra = 1000

# Generar una muestra aleatoria de la distribucion Poisson
muestra = np.random.poisson(lambda_param, tamanio_muestra)

# Crear el histograma de frecuencias
plt.hist(muestra, bins=max(muestra)-min(muestra)+1, rwidth=0.8, alpha=0.7)

# Configurar el grafico
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribucion de probabilidad Poisson')
plt.grid(True)

# Mostrar el grafico
plt.show()