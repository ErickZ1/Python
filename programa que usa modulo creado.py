#PROGRAMA QUE USA MODULO CREADO
import pepito, math
def resultado(x,y):
    if x == 1:
        print("La raíz cuadrada es", math.sqrt(y))
    elif x == 2:
        print("Elevado al cubo es", math.pow(y,3))
    else:
        print("El coseno es", math.cos(y))

while True:
    print("Ingrese  1)Raíz, 2)Potencia, 3)Coseno")
    tipo = pepito.veentero()
    if tipo <= 0 or tipo >3:
        break
    else:
        dato = pepito.vedecimal()
        resultado(tipo,dato)
        print()
