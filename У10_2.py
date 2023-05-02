
n=int(input("vvedite 1 4islo  "))
k=int(input("vvedite 2 4islo  "))
s=dict()
if n>k:
    while n>=k:
      s[n]=n**n
      n-=1
else:
   while n<=k:
      s[n]=n**n
      n+=1

print(s)
