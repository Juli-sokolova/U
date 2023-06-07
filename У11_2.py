import collections
kl1="kli4a"
vozr1="vozrast"
vid1="vid"
xoz1="xozain"

pets= {0:'0'}
def create():
    last = collections.deque(pets,maxlen=1)[0]
    last = last + 1
    return(last)

def pets_list(im):
    for key in im:
       print(f" kli4ke {key}")
       print(f"         Vid: {im[key]['vid']}")
       print(f"         Vozrast: {im[key]['vozrast']}")
       print(f"         Ima xozaina: {im[key]['xozain']}")

def read():
   for key in pets:
       if key!=0:
            im=pets[key].copy()
            pets_list(im)

def delete(ID):
    if ID in pets.keys():
        del pets[ID]
    else:
        print("Net takogo ID")

def get_pet(ID):
    if ID in pets.keys():
        im=pets[ID].copy()
        for key in im:
            print(
                f"Eto {im[key]['vid']} po kli4ke {key}. Vozrast {im[key]['vozrast']}. Ima xozaina {im[key]['xozain']}.")
    else:
        print("Net takogo ID")

def get_suffix(age):
    if age%10==1:
        age1=str(age)+' god'
    if (age%10>=2) and (age%10<=4):
        age1 = str(age) + ' godA'
    if (age % 10 >= 5):
        age1 = str(age) + ' let'
    return(age1)

def update(ID):# не доделала  не обновляет
    if ID in pets.keys():
        kl=pets[ID].copy()
        kl[vozr1]=get_suffix(vozr)
        kl[vid1]=vid
        kl[xoz1]=xoz
    else:
        print("Net takogo ID")

command=''
while command!='stop':
    pit=input("4erez ' ' kl, vozr, vid, xoz ").split()
    kl=pit[0]
    vozr=int(pit[1])
    vid=pit[2]
    xoz=pit[3]

    op=input("d-dobavit, i-izmenit ")
    if op=='d':
        key=create()
        pets[key] = {}
        pets[key][kl]={}
        pets[key][kl][vozr1]=get_suffix(vozr)
        pets[key][kl][vid1]=vid
        pets[key][kl][xoz1]=xoz
    elif op=='i':
        update(int(input("ID -")))

    command=input('stop-zakn4it, d-dalee ')
q='j'
while q!="exit":
    q=input("id- po ID; d - udaliti po ID; exit - bse,")
    if q=='id':
        get_pet(int(input("ID -")))
    if q == 'd':
        delete(int(input("ID -")))
    if q=='exit':
        print(read())

