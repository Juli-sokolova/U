class cherepachka:
    def __init__(self, x,y,s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self,s):
        self.y=self.y+s
        print(f"y {self.y}")
    def go_down(self,s):
        self.y = self.y - s
        print(f"y {self.y}")
    def go_left(self,s):
        self.x=self.x=s
        print(f"x {self.x}")
    def go_right(self,s):
        self.x=self.x+s
        print(f"x {self.x}")
    def evolve(self,s):
        self.s+=1
        print(f"{self.s}")
    def degrade(self,s):
        if (self.s-1)<=0:
            print("oxibka s<=0")
        else:
              self.s-=1
              print(f"{self.s}")

    def count_moves(self,x2, y2):
        a = 0
        while self.x >x2:
            a+=1
            tartila.go_left(self.s)
        while self.x <x2:
            a+=1
            tartila.go_right(self.s)
        while self.y >y2:
            a+=1
            tartila.go_down(self.s)
        while self.y <y2:
            a+=1
            tartila.go_up(self.s)
        print("min chagiv ", str(a))



x=int(input("Vvidite x "))
y=int(input("Vvidite y "))
s=int(input("Vvidite s kletok "))

x2=int(input("Vvidite x2 "))
y2=int(input("Vvidite y2 "))

tartila = cherepachka(x,y,s)
tartila.count_moves(x2, y2)




