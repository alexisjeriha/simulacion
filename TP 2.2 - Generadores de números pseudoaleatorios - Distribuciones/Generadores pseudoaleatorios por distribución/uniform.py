# Importe de librerías
import random
import matplotlib.pyplot as plt

#Definición de funciones
def uniform(a, b, u):
    uniform_random = a + (b - a) * u
    return uniform_random

#INICIA PROGRAMA PRINCIPAL

#Definición de variables y listas

n = 50 #cantidad de números a generar

a = 10 #cota inferior
b = 20 #cota superior

for i in range(n):
    random_number = random.random () 
    uniform_number = uniform(a, b, random_number)
    #Imprimo valores
    print(uniform_number)
