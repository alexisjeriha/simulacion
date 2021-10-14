# Importe de librerías
import random
import math

#Definición de funciones
def exponential(param, u):
    exponential_random = -(1 / param) * math.log(u)
    return exponential_random

#INICIA PROGRAMA PRINCIPAL

#Definición de variables

n = 50 #cantidad de números a generar
lambda_param = 1 #parámetro Lambda
for i in range(n):
    random_number = random.random ()
    uniform_number = exponential(lambda_param, random_number)
    #Imprime los valores
    print(uniform_number)

