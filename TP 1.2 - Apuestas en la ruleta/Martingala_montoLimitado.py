#Importe de librerías
import matplotlib.pyplot as plt
from random import randint

#ESTRATEGIA MARTINGALA - MONTO ILIMITADO - TIRADAS LIMITADAS (FLUJO DE CAJA)
#Condición éxito en la apuesta: el número es par

#Declaración de variables y arreglos
factor_apuesta = 2
cantidad_tiradas = 0
monto_inicial = 50
monto = monto_inicial
proxima_apuesta = 1
#lst_numeros = []
lst_montos = [monto] #Eje Y
lst_cantidad_tiradas = [cantidad_tiradas] #Eje X

while monto >= proxima_apuesta: #Tiene el monto necesario para realizar la apuesta
    valor_tirada = randint(0, 36) #Genera valor aleatorio entre 0 y 36
    cantidad_tiradas += 1
    #lst_numeros.append(valor_tirada) 
    if valor_tirada != 0 and valor_tirada % 2 == 0: #El número de la tirada es par y distinto de 0
        monto +=  proxima_apuesta
        proxima_apuesta = 1
    else: #El número de la tirada es impar
        monto -= proxima_apuesta
        proxima_apuesta *= factor_apuesta
    lst_cantidad_tiradas.append (cantidad_tiradas)
    lst_montos.append (monto) 
    if monto > monto_inicial: 
        plt.plot (cantidad_tiradas,monto, marker='o', color='green', markersize=4)
    else: 
        plt.plot (cantidad_tiradas,monto, marker='o', color='red', markersize=4)
  
#print("Los números que salieron son:",lst_numeros)

#Imprime en pantalla
print("-------------------------------------------------------------------")
print("> Se realizaron",cantidad_tiradas,"tiradas.")    
print ("> No puede realizar la apuesta de",proxima_apuesta,"porque le restan", monto, "fichas.")
print("-------------------------------------------------------------------")

#Defino título del gráfico y etiquetas
plt.title("Estrategia Martingala: Apuesta a número par")
plt.xlabel("Numero de tiradas")
plt.ylabel("Monto ($)")

#Muestro gráfico
plt.plot (lst_cantidad_tiradas, lst_montos, color='black', linewidth=1)
plt.plot (cantidad_tiradas,monto, marker='o', color='black', label='No puede duplicar apuesta')

plt.axhline (y=monto_inicial, color = 'blue', label='Monto inicial')
plt.legend()
plt.grid()
plt.show()  


        



