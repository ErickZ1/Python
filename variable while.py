#Ejemplos de while
#con variables
x = 1
while x < 10:
    print("Hola mundo, x vale",x)
    x += 1
print("Se termino el programa,  el valor de x es",x)
print()
#con una condicion fija
while True:
    print("Buenas noches Alumnos")
    dato = input("Ingresa FIN para terminar")
    if dato == "FIN":
        break
print("Se termino porque pulso la tecla fin")
print()
# con un valor que el usuario ingresa
num = int(input("Ingresa un numero entero: "))
while num >=0:
    print("Este texto se volvera a repetir")
    num = int(input("Ingresa un numero entero: ")) 
