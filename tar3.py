Person1 = float(input("Inversion de la primera persona: ")) 
Person2 = float(input("Inversion de la segunda persona: ")) 
Person3 = float(input("Inversion de la tercera persona: ")) 
Total = (Person1 + Person2 + Person3) 
Por1 = Person1 * 100 / Total 
Por2 = Person2 * 100 / Total 
Por3 = Person3 * 100 / Total
print()
print("Porcentajes de cada inversion")
print()
print("El Porcentaje de la inversion de la primera persona es : ", format(Por1,'0.2f'),"%") 
print("El Porcentaje de la inversion de la segunda persona es : ", format(Por2,'0.2f'),"%") 
print("El Porcentaje de la inversion de la tercera persona es : ", format(Por3,'0.2f'),"%") 
