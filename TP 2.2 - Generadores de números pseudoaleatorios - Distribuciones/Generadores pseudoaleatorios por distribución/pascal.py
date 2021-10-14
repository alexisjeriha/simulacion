# Importe de librerías
import random
import matplotlib.pyplot as plt
import math

#Definición de funciones
def pascal(k, q):
    tr = 1
    qr = math.log(q)
    for _ in range (k):
        r = random.random()
        tr *= r
    nx = (math.log(tr) / qr)
    x = nx
    return x

#INICIA PROGRAMA PRINCIPAL

#Definición de variables y listas

n = 50 #cantidad de números a generar
#Parámetros de la distribución de Pascal
r = 3 #número de éxitos
p = 0.4 #probabilidad de "éxito"

for i in range(n):
    x = pascal(r, p)
    #Imprimo valores
    print(x)

# x: número de ensayos para conseguir r éxitos de probabilidad p