#devuelve el minimo comun multiplo
def mcd(n,m):
    if n > m:
        mayorque = n
    else:
        mayorque = n
    while (mayorque % n != 0) or (mayorque % m != 0):
        mayorque += 1
    return(mayorque)

while True:
    x = int(input("Ingresa el primer numero:"))
    y = int(input("Ingresa el segundo numero:"))
    if x <= 0 or y <= 0:
        break
    else:
        z = mcd(x,y)
        print("El minimo comun multiplo es:",z)
        print()
