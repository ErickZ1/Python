#Entrada al parque Niño = 5 , Adulto Mayor = 0
entrada = int(input("Ingrese el número de entradas a comprar: "))
tipo = int(input("0 = Niño, 1 = Adulto, 2 = Adulto MAyor: "))
mensaje = 'Niño','Adulto','Adulto Mayor' #tipo conjunto 0,1,2....
if entrada < 1:
    print("No se puede comprar CERO entradas, ni tampoco negativo")
else:
    if tipo < 0 or tipo > 2:
        print("El tipo de persona no existe, verifique....")
    else:
        if tipo == 0:
            print("El niño tiene que estar acompañado de un Adulto")
        elif tipo == 1:
            print("El ingreso al parque hasta las 6 de la tarde")
        else:
            print("El ingreso es libre, Bienvenido al parque")
        print()
        print("El número de entradas compradas es ",entrada)
        print("La compra es para: ",mensaje[tipo])
