#Importe de librerías
import matplotlib.pyplot as plt
from random import randint

#ESTRATEGIA MARTINGALA
#Condición éxito en la apuesta: el número es par

#Declaración de variables y arreglos

tiradas = 1000
experimentos = 3

#lst_numeros = []
lst_n = range(1,tiradas+1) #Eje X
lst_fr = [] #Eje Y

for exp in range(experimentos):
    acumulador = 0
    lista = []
    for n in range(tiradas):
        valor_tirada = randint(0, 36) #Genera valor aleatorio entre 0 y 36      
        #lst_numeros.append(valor_tirada) 
        if valor_tirada != 0 and valor_tirada % 2 == 0: #El número de la tirada es par y distinto de 0
            acumulador += 1
        lista.append(acumulador/(n+1))
    lst_fr.append(lista)

#print("Los números que salieron son:",lst_numeros)

#Imprime en pantalla

#Defino título del gráfico y etiquetas
plt.title("Frecuencia relativa de obtener un número par según n")
plt.xlabel("n (número de tiradas)")
plt.ylabel("fr (frecuencia relativa)")

#Muestro gráfico
for i in range(experimentos):
    plt.bar(lst_n, lst_fr[i], alpha=0.4)
plt.axhline (y=(18/37), color='red', label='Frecuencia relativa esperada')
plt.ylim(0, 0.75)
plt.legend()
plt.grid()
plt.show()  