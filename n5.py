#ejemplo e una funcion que cree una lista de alumnos
def alumno(nombre):
    milista.append(nombre)

milista = []        #creando una lista en blanco
while True:
    nom = input("Ingresa el nombre del alumno: ")
    if nom == "fin":
        print("El listado de alumnos es: ")
        print(milista)
        break
    else:
        alumno(nom)
