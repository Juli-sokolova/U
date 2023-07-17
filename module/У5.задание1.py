print("Vvedite zeloe chislo ")
ch=int(input())#запись числа
if (ch%2) ==0:
    chet='chislo chetnoe'
else :
    chet='chislo NE chetnoe'
if (ch>0):
    pol='cislo polohitelnoe (+)'
elif (ch<0):
    pol='cislo otrezatelnoe (-)'
else:
   pol='cislo nulivoe (0)'


print(pol,' i ',chet)
