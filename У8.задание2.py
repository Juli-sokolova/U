print("Vvedite N ")
n=int(input())
res=[]
print("Vvedite N cisel v stroku cerez probel ")
res=input().split()
if len(res)<n:#Надо ли писаисать проверку на правельный ввод
    print("malo")
elif len(res)>n:
    print("mnogo")
elif len(res)==n:
    print ("ishodnii ",res)
    #print(res[n-1])
    res.insert(0,res[n-1])
    res.pop()
    print("inig     ",res)