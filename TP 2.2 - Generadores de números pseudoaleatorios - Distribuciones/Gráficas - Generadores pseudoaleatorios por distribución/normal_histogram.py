import random
import math
import matplotlib.pyplot as plt
import scipy.stats as sp
import numpy as np


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


#plt.plot(np.arange(-4, 4, 0.001), sp.norm.pdf(range,0,1))
#plt.hist(yAxis, bins=100, alpha=1, edgecolor = 'black',  linewidth=1)

count, bins, ignored = plt.hist(yAxis, 100, density=True, edgecolor='black')
plt.plot(bins, 1/((stddev * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mean)**2 / (2 * stddev**2)) ),
         linewidth=2, color='r')

plt.grid(True)
plt.show()
