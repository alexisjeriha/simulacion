import random
import math
import matplotlib.pyplot as plt
import numpy as np

def hypergeometric(tn, ns, p):
    x = 0
    for _ in range(ns):
        r = random.random()
        if (r-p) >= 0:
            s = 0
        else:
            s = 1
            x += 1
        p = (tn*p - s) / (tn - 1)
        tn -= 1
    return x
#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50000

#Parámetros de la distribución hipergeométrica
tn = 100000 #Total de elementos de la población
ns = 10 #Cantidad de elementos de la muestra
p =  0.2 #Proporción de elementos de la clase I sobre la población total
xAxis = []
yAxis = []

for i in range(n):
    x = hypergeometric(tn, ns, p)
    yAxis.append(x)

yAxis = np.array(yAxis)
bins = np.arange(0, yAxis.max() + 1.5) - 0.5

fig, ax = plt.subplots()
_ = ax.hist(yAxis, bins,  weights=np.zeros_like(yAxis) + 1. / len(yAxis), edgecolor='black')
ax.set_xticks(bins + 0.5)
plt.show()