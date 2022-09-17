#Muestra el monto ahorrado cada año
ahorro = float(input("Ingrese el monto inicial de ahorro: "))
interes = float(input("Ingrese la tasa de interes anual: "))
tiempo = int(input("Ingrese el número de años a ahorrar: "))
if tiempo <= 0 or interes <= 0:
    print("Error.... no puede ahorrar CERO años o interes no puede ser CERO")
else:
    for i in range(tiempo):
        ahorro *= 1 + interes / 100  #Ahorro = ahorro * (ahorro * interes / 100)
        print("El nuevo ahorro despues de "+str(i+1)+" años es", round(ahorro,2))
