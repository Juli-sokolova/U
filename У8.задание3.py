print("Vvedite max massu")
m=int(input())
print("Vvedite kolocestvo ribakov")
n=int(input())
kg =[]
for i in range(n):
    print("Vvedite massu riboka  ",i+1)
    v=int(input())
    if (v>=1) and (v<=m):
        kg.append(v) #���� ������ �� ����� ���� ��������� � ����� ������, ���� ������� ���, ����� ������� ��� ������ ���������
    else:
        print("ne korektnaa massa. Po umilcaniu A",i,"=1")
        kg.append(1)#�������� ��� �������� ����� �� ��������� 1
l=0
#kg.sort()

if (sum(kg)%m)!=0:
    l=(sum(kg)//m)+1
elif (sum(kg)%m)==0:
    l=(sum(kg)//m)

   

print ("min kolicestvo lodok = ",l)
