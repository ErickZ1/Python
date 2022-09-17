#programa que muestra el total de creditos de diferentes cursos
cursos = {'Matematicas':6,'Fisica':4,'Quimica':5,'Ingles':8}
total = 0
for nom, cre in cursos.items():
    print(nom,end-" ")
    total += cre
print("")
print("El total de creditos es",total)
