print("Vvedite stroku ")
slovo=input()#запись строки
l=list(slovo)#пиребирает каждую букву
ai=0 
ei=0 
ii=0
oi=0
ui=0
n=0
for i in l:#цикл переберает значения по одному, затем сравниваем с нужной буквой
    if i=='a':
        ai+=1
    elif i=='e':
        ei+=1
    elif i=='i':
        ii+=1
    elif i=='o':
        oi+=1
    elif i=="u":
        ui+=1
    else:
        n+=1
print("soglasnix - ",n," glasnix - ",ai+ei+ii+oi+ui)

if (ai==0) or (ei==0) or (ii==0) or (oi==0) or (ui==0):
    print("False")
else:
    print("kolichestvo bukv glasnix")
    print("a -",ai," e -",ei," i -",ii," o-",oi," u -",ui)
# без цикла как то не получается. Не знаю как перебрать без цикла
