# Codigo para comparaciones de tiempo con diferentes entradas
# En las implementaciones

# Nombre: Nestor Herrera
# Carnet: 18-10796

from fibonacci43 import *
# Para medir tiempo
import time
# Para visualizar
import matplotlib.pyplot as plt

# Para medicion del tiempo transcurrido en la funcion
# f con el valor de n dado
def medirTiempo(f,n):
    inicio = time.time()
    f(n)
    fin = time.time()
    return fin - inicio

inputs = range(9, 99, 5)
# Para guardar los tiempos transcurridos
tiemposFibRecursivo = []
tiemposFibCola = []
tiemposFibIter = []

# Obtenemos los tiempos
for n in inputs:
    tiemposFibRecursivo.append(medirTiempo(fibRecursivo43, n))
    tiemposFibCola.append(medirTiempo(fibCola43aux, n))
    tiemposFibIter.append(medirTiempo(fibIter43, n))

# Graficamos
plt.plot(inputs, tiemposFibRecursivo, label='Recursivo estandar')
plt.plot(inputs, tiemposFibIter, label='Iterativo')
plt.plot(inputs, tiemposFibCola, label='Recursivo de cola')

plt.xlabel('n')
plt.ylabel('Tiempo (s)')
plt.title('Comparacion de tiempos de ejecucion')
plt.legend()

plt.savefig('comparaciones.png')
plt.show()