n=int(input("4islo n - "))
def fact(n):
    rez=1
    i=1
    while i<=n:
        rez=rez*i
        i+=1
    return(rez)

f=fact(n)
print(fact(n))
sp=[]
while f>=1:
    sp.append(fact(f))
    f -= 1

print(sp)



