#funciones que tienen math
import math
def valor(x):
    print("El numero elevado al cuadrado es: ",math.pow(x,2))
    print("El logaritmo en base 10 es: ",math.log10(x))
    print("La raíz cuadrada es: ",math.sqrt(x))
    print("El area del circulo es: ",math.pi * x ** 2)
    print("La tangente es: ",math.tan(x))

while True:
    x = float(input("Ingrese un numero: "))
    if x <= 0:
        print("Se termino el programa")
        break
    else:
        valor(x)
        print()
