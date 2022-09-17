#Estado civil
print("Ingresa tu estado civil: ")
estado = input("S)oltero ,C)asado ,V)iudo ,D)ivorsiado: ")
esta = estado.upper() #Aseguro que sea mayusculas
if esta =="S":
    print("Ud. es solter(a)")
elif esta =="C":
    print("Ud. esta casad(a)")
elif esta =="V":
    print("Us. es viudo(a)")
elif esta =="D":
    print("Ud. es divorsiado(a)")
else:
    print("No existe este tipo de estado civil")
