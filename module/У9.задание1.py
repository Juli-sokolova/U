print("Vvedite N")
n=int(input())
s =set()
print("Vvedite N cisel cerez probel")
st=input().split()
if len(st)!=n:
    print("ne verno kolicestvo zifr")
else:
    for i in range(len(st)):
       s.add(int(st[i]))
    print ("razlicnih elementov v mnohestve  -  ",len(s))
#print ("min kolicestvo lodok = ",s)
      