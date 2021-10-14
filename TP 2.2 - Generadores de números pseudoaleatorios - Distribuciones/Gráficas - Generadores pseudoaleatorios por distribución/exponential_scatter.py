# Importe de librerías
import random
import matplotlib.pyplot as plt
import math

#Definición de funciones
def exponential(param, u):
    exponential_random = -(1 / param) * math.log(u)
    return exponential_random

#INICIA PROGRAMA PRINCIPAL

#Definición de variables y listas
n = 50000
xAxis = []
yAxis = []
lambda_param = 1.5
for i in range(n):
    random_number = random.random ()
    xAxis.append(i)
    uniform_number = exponential(lambda_param, random_number)
    yAxis.append(uniform_number)

plt.title("Distribución exponencial")
plt.xlabel("N°")
plt.ylabel("Valor")

#Muestro gráfico
plt.scatter (xAxis, yAxis, s=2)

plt.legend()
plt.grid()
plt.show() 
