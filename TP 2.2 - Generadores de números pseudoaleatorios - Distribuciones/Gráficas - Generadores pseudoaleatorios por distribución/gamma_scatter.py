# Importe de librerías
import random
import matplotlib.pyplot as plt
import math

#Definición de funciones
def gamma(K, A):
    tr = 1
    for _ in range(K):
        r = random.random()
        tr *= r
    x = -math.log(tr)/A
    return x

#INICIA PROGRAMA PRINCIPAL

#Defino variables a utilizar
n = 50000
xAxis = []
yAxis = []

#Parámetros de la distribución gamma
k = 2
a = 2

for i in range(n):
    x = gamma(k, a)
    xAxis.append(i)
    yAxis.append(x)

plt.title("Distribución gamma")
plt.xlabel("N°")
plt.ylabel("Valor")

#Muestro gráfico
plt.scatter (xAxis, yAxis, s=2)

plt.legend()
plt.grid()
plt.show() 
