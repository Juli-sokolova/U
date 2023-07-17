print("Vvedite cisel cerez probel 1 spisok")
st1=input().split()
print("Vvedite cisel cerez probel 2 spisok")
st2=input().split()

a =set()
b =set()
c =set()
for i in range(len(st1)):
    a.add(int(st1[i]))
for i in range(len(st2)):
    b.add(int(st2[i]))   

c=a.intersection(b)
print(c)
print(len(c))