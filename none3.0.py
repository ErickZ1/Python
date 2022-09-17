#ejemplo devuelve e imprime el resultado de una operacon mat
def especial(a,b):
    return(a ** 2 + b ** 3)

while True:
    x = int(input("Ingrese el primer número: "))
    y = int(input("Ingrese el segundo número: "))
    if x < 0 or y <= 0:
        break
    else:
        print("El resultado es:",especial(x,y))
        print()
