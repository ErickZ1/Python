#tiemda de frutas
frutas = {'platano': 2.50, 'Manzana': 3.35, 'Pera': 2.85, 'Naranja': 3.25}
print(frutas)

total = 0
while True:
    kg = float(input("Ingrese cuantos vas a comprar: "))
    if kg <= 0:
        print("El total de la compra es", round(total,2))
        break
    else:
        fruta = input("Que fruta vas a comprar: ")
        if fruta in frutas: # Lo que hemos escrito si esta en el dicc
            print(kg, "Kilos de", fruta, "cuesta en total", round(frutas[fruta] * kg,2))
            total += frutas[fruta] * kg
        else:
            print("La fruta", fruta, "No esta en la lista")
