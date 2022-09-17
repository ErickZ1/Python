a = input("Ingrese el primer valor: ")
if a.isdigit()!=True:
    print("No es número")
else:
    b = input("Ingrese el segundo valor: ")
    if b.isdigit()!=True:
        print("No es número")
    else:
        suma = int(a)+int(b)
        print(f"La suma de a + b seria igual a {suma}")
        
