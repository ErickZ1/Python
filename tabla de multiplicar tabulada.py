#muestra tabla de multiplicar tabulada
Dato1 = int(input("Ingrese el primer valor: "))
Dato2 = int(input("Ingrese el segundo valor: "))
if Dato1 <= 0 or Dato2 <= 0:
    print("ERROR.... los valores no pueden ser CERO ")
else:
    for i in range(Dato1):
        for j in range(Dato2):
            print((i + 1) * (j + 1), end="\t")
        print("")
