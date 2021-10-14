# Importe de librerías
import random
import matplotlib.pyplot as plt
import math

#Definición de funciones
def gamma(K, A):
    tr = 1
    for _ in range(K):
        r = random.random()
        tr *= r
    x = -math.log(tr)/A
    return x

#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50000
xAxis = []
yAxis = []

#Parámetros de la distribución gamma
k = 9
a = 0.5

for i in range(n):
    x = gamma(k, a)
    xAxis.append(i)
    yAxis.append(x)

plt.hist(yAxis, bins=100, alpha=1, edgecolor = 'black',  linewidth=1)
plt.grid(True)
plt.show()
plt.clf()
