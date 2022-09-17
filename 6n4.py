import random
numeroAleatorios=[]
for i in range(10):
    aleatorio=random.randint(1,100)
    numeroAleatorios.append(aleatorio)
    
cantImpares=0
for numero in numeroAleatorios:
    if numero % 2 != 0:
        cantImpares += 1
print("Hay",cantImpares,"numeros impares")
