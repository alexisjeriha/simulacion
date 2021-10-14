import random
import math
import matplotlib.pyplot as plt
import numpy as np

def empirica(n):
    k = 0
    k_values = []
    p_values = []
    while (sum(p_values)<1):
        k += 1
        r = random.random()/n
        if (r < 1-sum(p_values)):
            k_values.append(k)
            p_values.append(r)
        else:
            k_values.append(k + 1)
            p_values.append( 1 - sum(p_values))
    return k_values, p_values
#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50

#Parámetros de la distribución empirica

k_values, p_values = empirica(n)
plt.plot(k_values, p_values)
plt.show()
