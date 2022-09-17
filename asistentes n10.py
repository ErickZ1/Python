#Muestra puntaje por numero de asistentes
asistentes = int(input("Ingrese el número de asistentes: "))
if asistentes < 0:
    print("No puede tener asistentes negativos")
else:
    if asistentes > 500:
        print("Tu evento fue un éxito")
    elif asistentes > 200:
        print("Tu evento es favorable y esta aceptable")
    elif asistentes > 50:
        print("Tu evento no causo expectativa....")
    else:
        print("Te falto mayor publicidad para tu evento")
    print("El monto recaudado fue ",asistentes * 10,"soles")
