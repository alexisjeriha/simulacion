import random
import math
import matplotlib.pyplot as plt

a1, a3, a5, a7, a9 = (3.949846138, 
                      0.252408784,
                      0.076542912,
                      0.008355968,
                      0.029899776)

def normal():
    sum = 0
    for _ in range(12):
        sum += random.random()
        y = (sum - 6) / 4
    z = a1*y + a3*y**3 + a5*y**5 + a7*y**7 + a9*y**9
    return z

#INICIA PROGRAMA PRINCIPAL

n = 50000
xAxis = []
yAxis = []

#Defino parámetros de la distribución normal
mean, variance = (0, 1)
stddev = math.sqrt(variance)

for i in range(n):
    xAxis.append(i)
    x = normal() * stddev + mean
    yAxis.append(x)

plt.scatter (xAxis, yAxis, s=2)

plt.axhline(y=mean, c='black', lw=1, label='Esperanza matemática')
plt.axhline(-3*stddev, c='red', label='+- 3 desvios estándares', alpha=0.3)
plt.axhline(3*stddev, c='red', alpha=0.2)
plt.legend()
plt.grid()
plt.show() 