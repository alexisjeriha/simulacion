#Importe de librerías
import matplotlib.pyplot as plt
from random import randint

#ESTRATEGIA D'ALEMBERT - MONTO ILIMITADO - TIRADAS LIMITADAS (FLUJO DE CAJA)
#Condición éxito en la apuesta: el número es par

#Declaración de variables y arreglos

n = 0
cantidad_tiradas = 50
capital_inicial = 0
capital_neto = capital_inicial
proxima_apuesta = 1
lst_numeros = []
lst_capital_neto = [capital_neto] #Eje Y
lst_n = [n] #Eje X

for i in range(cantidad_tiradas):
    valor_tirada = randint(0, 36) #Genera valor aleatorio entre 0 y 36
    n += 1
    lst_numeros.append(valor_tirada) 
    if valor_tirada % 2 == 0 and valor_tirada != 0: #El número de la tirada es par y distinto de 0
        capital_neto += proxima_apuesta
        if proxima_apuesta > 1:
            proxima_apuesta -= 1             
    else: #El número de la tirada es impar o 0
        capital_neto -= proxima_apuesta
        proxima_apuesta += 1
    lst_n.append (n)
    lst_capital_neto.append (capital_neto)
    if capital_neto > capital_inicial: 
        plt.plot (n,capital_neto, marker='o', color='green', markersize=3)
    else: 
        plt.plot (n,capital_neto, marker='o', color='red', markersize=3)

print("Los números que salieron son:",lst_numeros)

#Imprime en pantalla

#Defino título del gráfico y etiquetas
plt.title("Estrategia D'Alembert: Apuesta a número par")
plt.xlabel("Numero de tiradas")
plt.ylabel("capital_neto ($)")

#Muestro gráfico
plt.plot (lst_n, lst_capital_neto, color='black', linewidth=1)
plt.axhline (y=capital_inicial, color='blue')
plt.legend()
plt.grid()
plt.show() 