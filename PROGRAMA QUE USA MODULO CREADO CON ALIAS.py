#PROGRAMA QUE USA MODULO CREADO CON ALIAS
import pepito as mio
def muestra(x,y):
    if  x > 100:
        print("El resultado es", x - y)
    else:
        print("El resultado es", x + y)

while True:
    dato = mio.veentero()
    num = mio.vedecimal()
    if dato == 0 or num == 0:
        print("Se termino el programa")
        break
    else:
        muestra(dato,num)
        print()
        
