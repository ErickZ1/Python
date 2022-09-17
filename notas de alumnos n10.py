#Muestra mensaje segun calificacion de alumno
nota = float(input("Ingresa la calificación final del alumno: "))
if nota < 0 or nota > 20:
    print("Las calificaciones no pueden ser negativas ni mas de 20 ")
else:
    if nota > 18:
        print("El alumno es excelente")
    elif nota > 14:
        print("El alumno es bueno")
    elif nota > 11:
        print("El alumno es regular")
    else:
        print("El alumno necesita regulación")
