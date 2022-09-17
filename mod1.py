#programa que importa solo 5 funciones matematicas
from math import sin, cos, tan, exp, log
def calcula(n):
    print("El seno es: ",sin(n))
    print("El coseno es: ",cos(n))
    print("La tangente es: ",tan(n))
    print("Exponencial es: ",exp(n))
    print("El logaritmo es: ",log(n))

while True:
    x = int(input("Ingrese un numero entero: "))
    if x <= 0:
        print("Se termino el programa")
        break
    else:
        calcula(x)
        print()
