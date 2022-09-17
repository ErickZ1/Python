#calcula el promedio de notas
print("Ingrese la calificacion del alumno para terminar")
nota = float(input("Ingresa nota: "))
total = 0
contar = 0

while nota != -1:
    if nota <= 20 and nota >=0:
        total += nota
        contar += 1
    else:
            print("La nota ingresada es mayor a 20, no se promedia")
            
    print("Ingrese la calificacion del alumno, -1 para terminar")
    nota = float(input("Ingresa nota: "))

print("El promedio de nota es: ",round(total / contar,2))
