print("Vvedite chislo A ")
a = int(input())
print("Vvedite chislo B ")
b = int(input())
rez=""
while a<b-1:
    if a%2==0:
        rez=rez+" "+str(a)#формирую стоку вывода, перевод из числа в строку
    a+=1
print(rez)
