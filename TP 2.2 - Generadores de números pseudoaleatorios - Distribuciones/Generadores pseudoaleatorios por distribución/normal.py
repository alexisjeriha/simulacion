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

#Defino variables a utilizar
n = 50

#Parámetros de la distribución normal
mean, variance = (0, 1) # caso Normal Estándar
stddev = math.sqrt(variance)

for i in range(n):
    x = normal() * stddev + mean
    #Imprimo valores
    print(x)
