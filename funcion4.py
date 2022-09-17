#En un programa puede existir mas de una funcion
def areacirculo(radio):
    pi = 3.1416
    print("El area del circulo es:",pi * radio ** 2)

def areacuadrado(lado):
    print("El area del cuadrado es:",lado * lado)

def areatriangulo(base, altura):
    print("El area del triangulo rectangulo es:",base * altura / 2)

while True:
    x = int(input("1=Circulo, 2=Cuadrado, 3=Rectangulo:"))
    if x <= 0 or x > 3:
        break
    else:
        y = int(input("Ingrese un número:"))
        if x == 1: #Area del circulo
            areacirculo(y)
        elif x == 2: #Area del cuadrado
            areacuadrado(y)
        else:
            z = int(input("Ingrese la altura del triangulo:"))
            areatriangulo(y,z)
        print()
