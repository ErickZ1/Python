lista_clientes=[]
cantClientes=int(input("Cuatos clientes quiere agregar: "))
for i in range(cantClientes):
    clientes=input("Ingrese el nombre del cliente:")
    lista_clientes.append(clientes)
print(lista_clientes)
