#Encuentra una vocal el número de veces que se repite en un texto
frase = input("Ingresa un parrafo: ")
vocal = input("Ingresa que vocal deseas contar: ")
contador = 0
for i in frase:
    if i.upper() == vocal.upper():
        contador += 1    #contado = contador + 1
print("La vocal %s se repite %i en el parrafo %s"%(vocal,contador,frase))
