import random
import math
import matplotlib.pyplot as plt

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
n = 50

#Parámetros de la distribución hipergeométrica
tn = 100000 #Total de elementos de la población
ns = 10 #Cantidad de elementos de la muestra
p =  0.2 #Proporción de elementos de la clase I sobre la población total

for i in range(n):
    x = hypergeometric(tn, ns, p)
    #Imprimo valores
    print(x)
