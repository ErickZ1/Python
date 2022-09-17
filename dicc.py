monedas = {'Euro': 'Europa', 'Dolar': 'EEUU', 'Sol': 'Perú', 'Yen': 'Japon'}
for tipo,pais in monedas.items():
    print(tipo,end=" ")
print("")

while True:
    mon = input("Ingrese el tipo de moneda: ")
    if mon == "fin":
        print("Se termino el programa")
        break
    else:
        print(monedas.get(mon.title(),"El país no esta registrado"))
