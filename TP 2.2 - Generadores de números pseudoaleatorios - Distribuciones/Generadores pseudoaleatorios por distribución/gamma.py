import random
import math
import matplotlib.pyplot as plt

def gamma(K, A):
    tr = 1
    for _ in range(K):
        r = random.random()
        tr *= r
    x = -math.log(tr)/A
    return x

#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50

#Parámetros de la distribución gamma
k = 2
a = 2

for i in range(n):
    x = gamma(k, a)
    #Imprimo valores
    print(x)
