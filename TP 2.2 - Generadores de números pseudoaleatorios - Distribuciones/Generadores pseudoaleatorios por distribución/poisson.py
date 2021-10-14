# Importe de librerías
import random
import math

#Definición de funciones
def poisson(p):
    x = 0
    b = math.exp(-p)
    tr = 1
    r = random.random()
    tr *= r
    while (tr - b) >= 0:
        r = random.random()
        tr *= r
    return x    

#INICIA PROGRAMA PRINCIPAL

#Definición de variables

n = 50 #cantidad de números a generar
lambda_param = 10 #parámetro Lambda
for i in range(n):
    x = poisson(lambda_param)
    #Imprime los valores
    print(x)

