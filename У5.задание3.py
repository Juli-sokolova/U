print("MIN summa investizii ")
inv=int(input())#������ ��� ��������
print("Kol $ u MIKL")
m=int(input())
print("Kol $ u IVAN")
i=int(input())
c=0 # ��� �������� ��� � ������ ������� �������
if (m>=inv) and (i>= inv):
    print("2")
else:
    if (m>=inv) and inv:
       print("MIKL")
       c+=1
    if (i>=inv) and (m<inv):
       print("IVAN")
       c+=1
if c==0:# ������� ��� �� � ������ �� ������ �� �������
    if (m+i)>=inv:
        print("1")
    else:
        if (m<inv) or (i<inv):#����� ������� �� ���������
            print("0")