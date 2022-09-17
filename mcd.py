#calcula el maximo comun divisor
def mcd(n,m):
    rest = 0
    while (m > 0):
        rest = m
        m = n % m    #encontrar si es par o impar 0 y 1
        n = rest
    return(n)
while True:
    x = int(input("Ingresa el número menor:"))
    y = int(input("Ingresa el número mayor:"))
    if x <= 0 or y <= 0:
        break
    else:
        z = mcd(x,y)
        print("El maximo común divisor es:",z)
        print()
