#Importe de librerías
import matplotlib.pyplot as plt
from random import randint

#ESTRATEGIA D'ALEMBERT - MONTO LIMITADO - TIRADAS ILIMITADAS
#Condición éxito en la apuesta: el número es par

#Declaración de variables y arreglos

n = 0
monto_inicial = 50
monto = monto_inicial
proxima_apuesta = 1
#lst_numeros = []
lst_montos = [monto] #Eje Y
lst_n = [n] #Eje X

while monto >= proxima_apuesta: #Tiene el monto necesario para realizar la apuesta
    valor_tirada = randint(0, 36) #Genera valor aleatorio entre 0 y 36
    n += 1
    #lst_numeros.append(valor_tirada) 
    if valor_tirada != 0 and valor_tirada % 2 == 0: #El número de la tirada es par y distinto de 0
         monto += proxima_apuesta
         if proxima_apuesta > 1:
             proxima_apuesta -= 1             
    else: #El número de la tirada es impar
        monto -= proxima_apuesta
        proxima_apuesta += 1
    lst_n.append (n)
    lst_montos.append (monto)
    if monto > monto_inicial: 
        plt.plot (n,monto, marker='o', color='green', markersize=3)
    else: 
        plt.plot (n,monto, marker='o', color='red', markersize=3)  
  
#print("Los números que salieron son:",lst_numeros)

#Imprime en pantalla
print("-------------------------------------------------------------------")
print("> Se realizaron",n,"tiradas.")    
print ("> No puede realizar la apuesta de",proxima_apuesta,"porque le restan", monto, "fichas.")
print("-------------------------------------------------------------------")

#Defino título del gráfico y etiquetas
plt.title("Estrategia D'Alembert: Apuesta a número par")
plt.xlabel("Numero de tiradas")
plt.ylabel("Monto ($)")

#Muestro gráfico
plt.plot (lst_n, lst_montos, color='black', linewidth=1)
plt.axhline (y=monto_inicial, color='blue')
plt.plot (n,monto, marker='o', color='black', label='No puede aumentar apuesta')
plt.legend()
plt.grid()
plt.show() 