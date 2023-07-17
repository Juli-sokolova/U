class kassa:
    def __init__(self, dengi):
        self.dengi = dengi

    def go_up(self,x):
        self.dengi=self.dengi+x
        print(f"v kase {self.dengi}")

    def count_1000(self):
        print (f"{self.dengi//1000}")

    def take_away(self,x):
        if self.dengi<x:
            print("malo deneg")
        else:
            a=self.dengi-x
            print(f"zabrali {x} deneg, ostalos {a}")

st=int(input("pervono4alnoe kolil deneg "))
denga = kassa(st)

vi=input("p- popolnit; v-vivod tisa4; z-zabrat iz kasssi ")
if (vi=='p') or (vi=='z'):
    d = int(input("x deneg - "))
    if vi=='p':
        denga.go_up(d)
    else:
        denga.take_away(d)
elif vi=='v':
    denga.count_1000()
else:
    print("oxibka")





