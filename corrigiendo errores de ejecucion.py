#CORRIGIENDO LOS ERRORES DE JECUCION
import math
def verificar():            #verifica que sea un numero
    while True:
        try:
            n = float(input("Ingresa un número: "))
            return(n)
        except ValueError:
            print("Solo se permite ingresar números.....")

while True:
    x = verificar()
    if x <= 0:
        break
    else:
        print("La raíz cuadrada es: ", math.sqrt(x))
        print()
