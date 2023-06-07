class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = 50

    def viv(self):
        print(f"Nazvanie avto: {self.name} . Skorost: {self.max_speed} Probeg: {self.mileage}")

    def seating_capacity(self, capacity):
        return f"Vmestitelnist 1 avtobusa {self.name} {capacity} pasaxirov"


st=input("Vvidite name ")
sk=int(input("Vvidite max skorost "))
pr=int(input("Vvidite pro "))
Autobus = Transport(st,sk,pr)

p=input( "Vmestitelnost avtobusa izmenit (da, net)")
if p=="da":
    vm=int(input("Vvidite vmestitelnost "))
    Autobus.capacity =vm
elif p=="net":
    vm = Autobus.capacity

Autobus.viv()
print(Autobus.seating_capacity(vm))


