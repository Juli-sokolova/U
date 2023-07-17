print("Vvedite chislo: ")
num = int(input())
c = 0

for i in range(1, num+1):
    if num % i == 0:
        c += 1

print("kolicestvo delitelei ",num, " = ", c)