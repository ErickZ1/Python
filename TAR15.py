class Vehiculo():
    def encender(self):
        print("El vehiculo esta encendido")
    def avanzar(self):
        print("El vehiculo esta avanzando en 4 ruedas")
    def frenar(self):
        print("El vehiculo esta frenando")
class Camion(Vehiculo):
    def avanzar(self):
        print("El Vehiculo pesado esta avanzando en 8 ruedas")
miCamion=Camion()
miCamion.encender()
miCamion.avanzar()
miCamion.frenar()
