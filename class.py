#creando nuestra primera clase
class humano():
    def  __init__(self, edad, nombre, ocupación):  #definiendo campos
        self.edad  = edad
        self.nombre = nombre
        self.ocupación = ocupación

    def presentar(self):          # MOSTRAR INFORMACIÓN DE LA TABLA
        presenta = ("Hola soy {}, mi edad es {} y mi ocupación es {}")
        print(presenta.format(self.nombre, self.edad, self.ocupación))

    def modifica(self, puesto):   #MODIFICA EL DATO OCUPACIÓN
        self.puesto = puesto
        mensaje = ("{} ha sido contratado como {}")
        print(mensaje.format(self.nombre, self.puesto))
        self.ocupación = puesto  #AQUI SE ESTA MODIFICANDO LA TABLA
perso1 = humano(35,"Manuel","Instructor")  #OBJETOS AGREGANDO A LA TABLA
perso2 = humano(19,"Carlos","Cocinero")
perso3 = humano(31,"Oscar","Taxista")
perso2.presentar()
perso3.presentar()
perso1.presentar()
perso1.modificar("Jardinero")
perso2.modificar("Gerente")
perso1.presentar()
perso2.presentar()
x = input("¿Cual es el nuevo puesto de trabajo?")
perso3.modificar(x)
perso3.presentar()
