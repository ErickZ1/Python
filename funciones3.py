#Ejemplo de pasar varios valores
def cuadrado(*ejemplo):
    list = []
    for i in ejemplo:
        list.append(i ** 2)
    print("El cuadrado de los números",*ejemplo)
    print("Elevado al cuadrado",list)
    print()

cuadrado(2, 4)
cuadrado(6, 8, 10, 12, 14)
cuadrado(1, 3, 5, 7, 9, 11, 13, 15, 17, 20)
cuadrado(3.67, 7.89, 12.23)
