#Muestra la longitud de un texto
texto = input("Ingresa un texto (Maximo 250 carcteres) ")
tipo = input("Quieres en M)ayusculas o m)inusculas ")
longitud = len(texto) #cuenta cuantos carcteres tiene un texto
if longitud > 20:
    print("Tu deberias ser un escritor famoso ")
    print("Tu testo es muy bueno ")
    if tipo == "M":
        print("Tu texto en mayusculas: ",texto.upper())
    else:
        print("Tu texto en minusculas: ",texto.lower())
else:
    print("Tu texo es pequeño ")
    print("Deberias ser matematico ")
