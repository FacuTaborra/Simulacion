import numpy as np
import matplotlib.pyplot as plt

#NORMAL

# Parámetros de la distribución normal
media = 0
desviacion_estandar = 1
tamaño_muestra = 1000

# Generar una muestra aleatoria de la distribución normal
muestra = np.random.normal(media, desviacion_estandar, tamaño_muestra)

# Crear el histograma
plt.hist(muestra, bins='auto', density=True, alpha=0.7, rwidth=0.85)

# Calcular la función de densidad de probabilidad (PDF)
rango = np.linspace(media - 3 * desviacion_estandar, media + 3 * desviacion_estandar, 100)
pdf = 1 / (desviacion_estandar * np.sqrt(2 * np.pi)) * np.exp(-(rango - media)**2 / (2 * desviacion_estandar**2))

# Graficar la función de densidad de probabilidad
plt.plot(rango, pdf, color='r')

# Configurar el gráfico
plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución de probabilidad normal')
plt.grid(True)

# Mostrar el gráfico
plt.show()
