#Muestra las veces que haz cumplido años
edad = int(input("Ingresa tu edad: "))
if edad <= 0 or edad > 120:
    print("ERROR no puede tener edad negativa, cero a mayor a 120")
else:
    for i in range(edad):
        print("Has cumplido "+str(i+1)+" años")
