#Termina cuando ingresa la palabra secreta
while True:
    texto = input("Ingresa un texto cualquiera: ")
    if texto.upper() == "FIN":
        break
    print("Felicitaciones encontro la palabra secreta")
