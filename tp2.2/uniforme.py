import random
import matplotlib.pyplot as plt

def generar_numero_uniforme(a, b):
    return random.uniform(a, b)

a = 0  # Límite inferior
b = 10  # Límite superior
numeros = []

# Generar 100 números pseudoaleatorios en la distribución uniforme
for i in range(100):
    numero = generar_numero_uniforme(a, b)
    numeros.append(numero)
    plt.scatter(i+1, numero, color='b')

# Gráfica de frecuencia
plt.figure()
plt.hist(numeros, bins=10, edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Distribución Uniforme')

# Configuración de la apariencia de la gráfica de dispersión
plt.figure()
plt.scatter(range(1, len(numeros)+1), numeros, color='b')
plt.xlabel('Número de Corrida')
plt.ylabel('Valor')
plt.title('Distribución Uniforme')

# Mostrar ambas gráficas
plt.show()
