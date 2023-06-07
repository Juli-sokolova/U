import random
n=int(input("stroka n -  "))
m=int(input("stolbik m -  "))

A= [ [ random.randint(1, 9) for j in range(m)] for i in range(n) ]
B= [ [ random.randint(1, 9) for j in range(m)] for i in range(n) ]


print('A:')
for i in range(n):
    print(A[i])
print('B:')
for i in range(n):
    print(B[i])

# iterate through rows 
#for i in range(len(X)):
#   for j in range(len(X[0])):
#              C[i][j] = X[i][j] + Y[i][j]
C = [ [ A[i][j]+B[i][j] for j in range(m) ] for i in range(n) ]
print('C:')
for r in C:
      print(r)