#muestra si la palabra es un palindromo oso, somos, radar, seres, arenera
texto = input("Ingrese una palabra: ")
key = "fin"
while texto != key:
    guardado = texto
    texto = list(texto) #cambiando una palabra a un conjunto de caracteres
    guardado = list(guardado)   #sarten list(sarten) s a r t e n
    guardado.reverse()   #n e t r a s
    if guardado == texto:
        print("La palabra ingresada es un palindromo ")
    else:
        print("El texto no es un palindromo..... Intente otra vez")
    texto = input("Ingrese una palabra: ")

print("El programa termino porque escribio la palabra FIN")
