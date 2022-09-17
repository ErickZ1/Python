nom = input("Nombre completo del Trabajador: ") 
hrs = int(input("Horas de trabajo: ")) 
SalHor = float(input("Pago por hora: ")) 
Sueldo = SalHor * hrs 
Incre = Sueldo * 15 / 100 
Neto = Sueldo + Incre 
print("El Sueldo Bruto del Trabajador es  : ", format(Sueldo,'0.2f')) 
print("El Incremento del 15% es           : ", format(Incre,'0.2f')) 
print("El Neto a Cobrar por Trabajador es : ", format(Neto,'0.2f')) 
