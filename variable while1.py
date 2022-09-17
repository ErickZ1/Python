#verifica la contraseña y cuenta los intentos
clave = input("Ingresa tu contraseña: ")
key = "Virtual21"
contador = 1
while clave !=key:
    print("La contraseña ingresada no es valida...... intenta otra vez")
    contador +=1
    if contador == 4:
        break
    else:
        clave = input("Ingresa tu contraseña: ")

if contador == 4:
    print("No encontro la contraseña")
else:
    print("La contraseña fue encontrada en",contador,"intento")
