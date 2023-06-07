class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def viv(self):
        print(f"Nazvanie avto: {self.name} . Skorost: {self.max_speed} Probeg: {self.mileage}")

st=input("Vvidite name ")
sk=int(input("Vvidite max skorost "))
pr=int(input("Vvidite pro "))

Autobus = Transport(st,sk,pr)

Autobus.viv()


