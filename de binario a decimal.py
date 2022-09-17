#Cambia de bianrio 010101010 a decimal
def paradecimal(n):
    n = list(n) #texto se separa y se convierte en lista 1 0 1 0 1 0 1 0 1 0
    n.reverse()  #0 1 0 1 0 1
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return(decimal)

while True:
    x = input("Ingresa un numero binario 0 y 1:")
    if len(x) > 8 or x == "fin":
        break
    else:
        z = paradecimal(x)
        print("El binario de",x,"es",z)
        print()
