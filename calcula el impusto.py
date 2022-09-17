#Calcula el impuesto
def venta(valor):
    imp = valor * 0.19
    print("El valor de ventas es",round(valor,2),"soles")
    print("El impuesto es",round(imp,2),"soles")
    print("El total de la venta", round(valor + imp,2),"soles")
    return(valor + imp) #valor + imp = precio de venta

while True:
    x = float(input("Ingresa el valor de venta:"))
    if x <=0:
        break
    else:
        y = venta(x)        #obtengo el precio de venta
        z = y * 0.12
        print("El descuento 12% es", round(z,2),"soles")
        print("El precio  a pagar es", round(y - z,2),"soles")
        print()
