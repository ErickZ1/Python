p1 = input("Ingresa tu nombre : ")
APEL = input("Ingresa tu apellido paterno : ")
ape_mat = input("Ingresa tu apellido materno : ")
edad = int(input("Ingresa tu edad : "))
print();
print("Tu nombre es ", p1)
print("Tu apellido paterno al reves es ",APEL[::-1])
print("Tu apellido materno al reves es ",ape_mat[::-1])

print("Tu apellido materno es "+ ape_mat +" y tienes "+ str(edad) +" años")
print(f"Tu apellido materno es {ape_mat} y tienes {edad} años")
