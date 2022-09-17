#CREACION DE MODULO PEPEITO
def vedecimal():            #verifica que sea un numero
    while True:
        try:
            n = float(input("Ingresa un número entero o decimal: "))
            return(n)
        except ValueError:
            print("Solo números entero o decimal.....")

def veentero():            #verifica que sea un numero
    while True:
        try:
            n = float(input("Ingresa un número entero: "))
            return(n)
            break
        except ValueError:
            print("Solo se permite ingresar números.....")
