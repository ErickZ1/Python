#PROGRAMA CON ERROR DE EJECUCION
import math
def muestra(x):
    print("La raíz cuadrada es: ",math.sqrt(x))

while True:
    n = float(input("Ingrese un numero: "))
    if n <= 0:
        break
    else:
        muestra(n)
