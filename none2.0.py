#ejemplo none
def alumno(nota):
    if nota < 10.5:
        return("El alumno esta desaprobado")
    else:
        return("El alumno esta aprobado")

while True:
        n = float(input("Ingrese el promedio:"))
        if n < 0 or n > 20:
            break
        else:
            print(alumno(n))
            print()
