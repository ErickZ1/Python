#Encuentra si el numero es par o impar
numero = int(input("Ingresa un numero entre el 1 y 100: "))
X = numero % 2#Encontrando el resto de la division entera
if X == 0:
    print("El numero ingresado es Par ")
    print("El numero al cuadrado es: ",numero ** 2)
    print("La raiz cuadrada del numero es: ",numero ** (1/2))
else:
    print("El numero ingresado es Impar")
    print("El numero al cubo es: ",numero ** 3)
    print("La raiz cubica del numero es: ",numero ** (1/3))
