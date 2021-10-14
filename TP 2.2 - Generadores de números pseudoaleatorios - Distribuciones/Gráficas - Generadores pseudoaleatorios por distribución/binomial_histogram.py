import random
import math
import matplotlib.pyplot as plt
import numpy as np

def binomial(n, p):
    x = 0
    for _ in range(n):
        r = random.random()
        if (r - p) < 0:
            x += 1
    return x


    

#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50000

#Parámetros de la distribución binomial
n_e = 10
p = 0.3
xAxis = []
yAxis = []

for i in range(n):
    x = binomial(n_e, p)
    xAxis.append(i)
    yAxis.append(x)

plt.title("Distribución binomial")
plt.xlabel("N°")
plt.ylabel("Valor")

#Muestro gráfico
yAxis = np.array(yAxis)
bins = np.arange(0, yAxis.max() + 1.5) - 0.5

fig, ax = plt.subplots()
_ = ax.hist(yAxis, bins,  weights=np.zeros_like(yAxis) + 1. / len(yAxis), edgecolor='black')
ax.set_xticks(bins + 0.5)
plt.show()
