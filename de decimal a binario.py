#Cambia un número decimal a binario 0000 1111
def parabinario(n):
    binario = []    # lista de valores sin signo
    while n > 0:
        binario.append(str(n % 2)) #Resro  de divi entera 0,1
        n //= 2  # 128 -- 64 -- 32 -- 16
    binario.reverse()
    return ''.join(binario)

while True:
    x = int(input("Ingresa un numero entre 1 y 255:"))
    if x <= 0 or x >255:
        break
    else:
        z = parabinario(x)
        print("El numero",x,"En binario es",z)
        print()
