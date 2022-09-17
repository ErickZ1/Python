#$crear clases y subclases formas de transmitir herencias
class hijo:
    pass          #Este comando devuyelve true o faslse
class padre(hijo):
    pass
class abuelo(padre):
    pass
for x in [hijo,padre,abuelo]:
    for y in[hijo,padre,abuelo]:
        print(issubclass(x,y),end="\t")
    print()
