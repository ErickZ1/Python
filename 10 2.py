#Muestra el mensaje de aprobo o desaprobo el curso
nota1 = float(input("ingresa la nota 1: "))
nota2 = float(input("ingresa la nota 2: "))
nfinal = nota1 * 0.4 + nota2 * 0.6
if nfinal > 10.5:
    print("El alumno aprobo el cursom: ",nfinal)
if (nfinal > 0) and (nfinal < 10.5):
    print("El alumno desaprobo el curso: ",nfinal)
