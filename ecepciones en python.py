#ECEPCIONES EN PYTHON:DIVISION ENTRE CERO
def reciproco(n,m):
    try:
        n = m / n   #DEVUELVE LA DIVISION
    except ZeroDivisionError:
        print("No se puede dividir entre CERO")
        n = None
    else:
        print("Todo esta OK")
    finally:
        print("Retorna el resultado de la division")
        return(n)
while True:
     x = float(input("Ingrese el Dividendo"))
     if x <= 0:
        break
    else:
        y = float(input("Ingrese el Divisor:"))
        print(reciproco(y,x))
        print()
