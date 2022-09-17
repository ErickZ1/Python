# A quien le toca invitar la pizza
from random import choice
def invitar():
    personas = ["Quiroz","Sayas","María","Jorge","Acosta","Corman"]
    print("Le toca a: ",choice(personas))

while True:
    x = input("Quien invita la pizza (s/n): ")
    if x == "n":
        break
    else:
        invitar()
        print()
