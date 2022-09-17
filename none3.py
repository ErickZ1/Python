#Ejemplo que devuelve un dato de la lista pasando un número
def diasemana(n):    #crean lista el indice inicia en 0
    lista = 'Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'
    return(lista[n])
while True:
    num = int(input("Ingrese un número de día semanal (1-7): "))
    if num <= 0 or num > 7:
        print("Esos días no existen......")
        break
    else:
        print("El día de la semana es: ",diasemana(num-1))
        print()
        
