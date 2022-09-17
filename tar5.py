print("1.Suma\n2.Resta\n3.Multiplica\n4.Division\n5.Salir\t\t-- Ingrese la Opcion "); 
op = int(input("Favor de Ingresar la opcion que desea realizar: ")); 
while(op !=5): 
    num1 = float(input("Ingrese el primer dato numerico: ")); 
    num2 = float(input("Ingrese el segundo dato numerico : ")); 
    if(op == 1): 
        print("El Resultado de la Suma es : ",str(num1 + num2)) 
    elif(op == 2): 
        print("El Resultado de la Resta es : ",str(num1 - num2)) 
    elif(op == 3): 
        print("El Resultado de la Multiplicacion es : ",str(num1 * num2)) 
    elif(op == 4): 
        print("El Resultado de la Division es : ",str(num1 / num2)) 
    else: 
        break; 
    print("1.Suma\n2.Resta\n3.Multiplica\n4.Division\n5.Salir\t\t-- Ingrese la Opcion "); 
    op = int(input("Favor de Ingresar la opcion: ")); 
