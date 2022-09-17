#ejemplo de none
def parimpar (n):
    if (n % 2 == 0):
        return("Es un número par")
    else:
        return("El número es impar")

while True:
    num = int(input("Ingrese un número entero:"))
    if num <= 0:
        break
    else:
        print(parimpar(num))
        print()
