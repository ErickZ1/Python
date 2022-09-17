import random
numeroAleatorios=[]
for i in range(10):
    aleatorio=random.randint(1,100)
    numeroAleatorios.append(aleatorio)
    
cantPares=0
for numero in numeroAleatorios:
    if numero%2==0:
        cantPares+=1
print("Hay",cantPares,"numeros pares")
