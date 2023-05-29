import random
import matplotlib.pyplot as plt
import numpy as np

def generar_numero_exponencial(lam):
    return random.expovariate(lam)

lam = 0.5  # Parámetro lambda para la distribución exponencial
numeros = []

# Generar 100 números pseudoaleatorios con distribución exponencial
for i in range(100):
    numero = generar_numero_exponencial(lam)
    numeros.append(numero)
    plt.scatter(i+1, numero, color='b')

# Gráfica de frecuencia
plt.figure()
plt.hist(numeros, bins=10, edgecolor='black', density=True)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Distribución Exponencial')

# Configuración de la apariencia de la gráfica de dispersión
plt.figure()
plt.scatter(range(1, len(numeros)+1), numeros, color='b')
plt.xlabel('Número de Corrida')
plt.ylabel('Valor')
plt.title('Distribución Exponencial')

# Función de densidad teórica de la distribución exponencial
x = np.linspace(0, max(numeros), 100)
y = lam * np.exp(-lam * x)
plt.figure()
plt.plot(x, y, color='r')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.title('Función de Densidad Teórica')

# Mostrar todas las gráficas
plt.show()
