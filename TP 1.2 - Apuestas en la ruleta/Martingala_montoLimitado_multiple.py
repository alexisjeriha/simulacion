#Importe de librerías
import matplotlib.pyplot as plt
from random import randint

#ESTRATEGIA MARTINGALA - MONTO LIMITADO - TIRADAS ILIMITADAS - GRAFICAS MULTIPLES
#Condición éxito en la apuesta: el número es par

#Declaración de variables y arreglos
factor_apuesta = 2
monto_inicial = 50
experimentos = 5
lst_montos = [] #Eje Y
lst_n = [] #Eje X
for i in range(experimentos):
    monto = monto_inicial
    proxima_apuesta = 1
    n = 0
    lst_n_aux = []
    lst_montos_aux = []

    while monto >= proxima_apuesta: #Tiene el monto necesario para realizar la apuesta
        valor_tirada = randint(0, 36) #Genera valor aleatorio entre 0 y 36
        n += 1
        if valor_tirada % 2 == 0 and valor_tirada != 0: #El número de la tirada es par
            monto +=  proxima_apuesta
            proxima_apuesta = 1
        else: #El número de la tirada es impar
            monto -= proxima_apuesta
            proxima_apuesta *= factor_apuesta
        lst_n_aux.append (n)
        lst_montos_aux.append (monto)  
    lst_n.append(lst_n_aux)
    lst_montos.append(lst_montos_aux)
    plt.plot (n,monto, marker='o', color='black')
  
#print("Los números que salieron son:",lst_numeros)


#Defino título del gráfico y etiquetas
plt.title("Estrategia Martingala: Apuesta a número par")
plt.xlabel("Numero de tiradas")
plt.ylabel("Monto ($)")

#Muestro gráfico
for i in range(experimentos): #Plotea una gráfica para cada experimento
    plt.plot (lst_n[i], lst_montos[i], linewidth=1)
plt.axhline(y=monto_inicial, color='red', label="Monto inicial")
plt.legend()
plt.grid()
plt.show()  


        



