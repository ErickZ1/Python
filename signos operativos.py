#Este programa muestra los numeros complejos
a = float(input("Ingrese el Lado A: "))
b = float(input("Ingrese el Lado B: "))
c = (a ** 2 + b ** 2) ** (1/2)     #hipotenusa
x = 7
y = 2
z = 9
divnor = X / y      #Division normal 7 entre 2 = 3.5
divent = x // y     #Division Entero 7 entre 2 = 3
divres = x % y      #Resto de una division entera 7 % 2 = 1
sum3 = x + y + z    #Suma
res4 = z - y        #Resta
varios = x + y + z / x - y    #Primero va la Mult.Divis y despues Suma y Resta
print("La Hipotenusa es ",c)
print("La Div. Normal es ",divnor)
print("La Div. Entera es ",divent)
print("El Resto Div. Entera es ".divres)
print("La Suma es ",sum3)
print("La Resta es ",res4)
print("El resultado combinado es ",varios)
