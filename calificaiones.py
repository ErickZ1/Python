#Este programa calcula el puntaje y el promedio del alumno
N1 = float(input("Ingresa Nota 1 : "))
N2 = float(input("Ingresa Nota 2 : "))
N3 = float(input("Ingresa Nota 3 : "))
N4 = float(input("Ingresa Nota 4 : "))
N5 = float(input("Ingresa Nota 5 : "))
puntaje = N1 + N2 + N3 + N4 + N5
prom = puntaje / 5
print()
print("El puntaje del alumno es : ",puntaje)
print("El promedio es : ",prom)
print()
print("El puntaje del alumno es : ",format(puntaje,'0.0f'))
print("El promedio es : ",format(prom, '0.2f'))
