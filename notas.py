Nota1 = float(input("Ingrese la Nota1: "))
Nota2 = float(input("Ingrese la Nota2: "))
curso = int(input("Curso: 0 = Ingles, 1 = Quimica, 2 = Fisica, 3 = Informatica"))
nombres = 'Ingles','Quimica Elemental','Fisica aplicada','TIA'

if Nota1 == Nota2:
    print("Ambas calificaciones son iguales: ",Nota1,Nota2)
if Nota1 > Nota2:
    print("La Nota1 es mayor a la Nota2: ",Nota1)
if Nota2 > Nota1:
    print("La Nota2 es Mayor: ",Nota2)

print("El curso del alumno es",nombres[curso])
