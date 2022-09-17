#pizzeria Romana
tipo = 'Pizza Americana','Pizza Hawayana','Pizza Peperoni'
adicional = 'Mozzarella','Jamon','Doble queso en los bordes'
print("BIENVENIDOS A LA PIZZERIA ROMANA")
print("Escoja el tipo ",tipo)
tippiz = input("A)merica, H)awayana, P)eperoni: ")
print("Escoja el adicional ",adicional)
tipadi = input("M)ozzarella, J)amón, D)oble queso: ")

if tippiz.upper() == "A":
    print("Lleva Pizza Americana")
elif tippiz.upper() == "H":
    print("Lleva Pizza HAwayana")
elif tippiz.upper() == "P":
    print("Lleva Pizza Peperoni")
else:
    print("No lleva ninguna Pizza")

if tipadi.upper() == "M":
    print("Adiciona Mozarella")
elif tipadi.upper() == "J":
    print("Adiciona Jamón")
elif tipadi.upper() == "D":
    print("Adiciona doble queso")
else:
    print("No adiciona más")
