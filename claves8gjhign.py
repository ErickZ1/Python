clave = input("Ingresa tu contraseña : ")
opera = int(input("1 para Retiros, 2 para Pagos, 3 para Ahorros : "))
if opera == 1:
    print("Tu clave es para realizar pagos al contado...")
if opera == 2:
    print("Tu clave es para realizar pagos al contado...")
    print("Tu contraseña cifrada es : ",clave[::-1])
if opera == 3:
    print("Tu clave no es segura...")
    print("No puedes hacer depositos ")
    print("Te sale tres lineas impresas")
