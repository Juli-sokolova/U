print("Vvedite max massu")
m=int(input())
print("Vvedite kolocestvo ribakov")
n=int(input())
kg =[]
for i in range(n):
    print("Vvedite massu riboka  ",i+1)
    v=int(input())
    if (v>=1) and (v<=m):
        kg.append(v) #åñëè ââñåëè íå âåğíî íàäî âåğíóòüñÿ ê ââîäó çàíîâî, íàäî ôóíêöèş òóò, áóäåì ñ÷èòàòü ÷òî ââîäÿò ïğàâåëüíî
    else:
        print("ne korektnaa massa. Po umilcaniu A",i,"=1")
        kg.append(1)#çíà÷åíèå ïğè íåâåğíîì ââîäå ïî óìîë÷àíèş 1
l=0
#kg.sort()

if (sum(kg)%m)!=0:
    l=(sum(kg)//m)+1
elif (sum(kg)%m)==0:
    l=(sum(kg)//m)

   

print ("min kolicestvo lodok = ",l)
