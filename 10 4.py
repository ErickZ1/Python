#Encuentra la division de un numero
dendo = float(input("Ingrese el dividendo : "))
dsor = float(input("Ingrese el divisor : "))
if dsor == 0:
    print("No se puede realizar la divison entre CERO ")
    print("ERROR DE PROGRAMACION.......")
else:
    print("La division normal es : ",dendo / dsor)
    print("La division entera es : ",dendo // dsor)
    print("El resto de la divison entera es :", dendo % dsor)
