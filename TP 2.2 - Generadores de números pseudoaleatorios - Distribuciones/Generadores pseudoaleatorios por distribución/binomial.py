import random
import math
import matplotlib.pyplot as plt

def binomial(n, p):
    x = 0
    for _ in range(n):
        r = random.random()
        if (r - p) < 0:
            x += 1
    return x

#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50

#Parámetros de la distribución binomial
n_essay = 10 #ensayos de Bernoulli
p = 0.2 #probabilidad de "éxito"

for i in range(n):
    x = binomial(n, p)
    #Imprimo valores
    print(x)
