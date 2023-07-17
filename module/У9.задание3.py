print("Vvedite N cisel cerez probel")
st=input().split()
s =set()
for i in range(len(st)):
    
    if int(st[i]) in s:
        print(st[i]," yes")
    else:
        print(st[i]," no")
    s.add(int(st[i]))


