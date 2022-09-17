#Muestra un triangulo con numeros impar hasta el ingresado
n = int(input("Ingresa un numero impar, maximo 21: "))
if n % 2 == 0 or n <= 0 or n > 21:
    print("ERROR....el numero ingresado no corresponde ")
else:
    for i in range(1,n+1,2):
        for j in range(i,0,-2):
            print(j, end=" ")
        print("")
