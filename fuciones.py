#Mi primera función
def saludo(dato) :
    print("Hola",dato)

while True:
    x = input("Ingresa cualquier cosa: ")
    if x == "fin":
        break
    else:
        saludo(x)
        print()

print("Se termino el programa")
