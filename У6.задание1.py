print("Vedite cislo N")
N = int(input())
nili= 0
print("vodim N kolicestvo zelih cisel")
for i in range(N):
    i = int(input())
    if i == 0:
        nili += 1
print("kolicestvo vvedenix 0 -  ",nili)
