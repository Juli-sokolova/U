print("MIN summa investizii ")
inv=int(input())#запись мин вложений
print("Kol $ u MIKL")
m=int(input())
print("Kol $ u IVAN")
i=int(input())
c=0 # для проверки что у одного долоров хватает
if (m>=inv) and (i>= inv):
    print("2")
else:
    if (m>=inv) and inv:
       print("MIKL")
       c+=1
    if (i>=inv) and (m<inv):
       print("IVAN")
       c+=1
if c==0:# условие что ни у одного по одному не хватает
    if (m+i)>=inv:
        print("1")
    else:
        if (m<inv) or (i<inv):#можно условия не проверять
            print("0")