list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def v(l,i):
    if i<len(l):
        print(l[i])
        i+=1
        v(l,i)
    else:
        print("bce")

v(list,i=0)