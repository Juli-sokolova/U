kl1="kli4a"
vozr1="vozrast"
vid1="vid"
xoz1="xozain"

pets= {}

c=''
while c!='z':
    pit=input("4erez ' ' kl, vozr, vid, xoz ").split()
    kl=pit[0]
    vozr=int(pit[1])
    vid=pit[2]
    xoz=pit[3]

    pets[kl]={}
    if vozr%10==1:
        l=str(vozr)+' god'
    elif (vozr%10)>=2 and (vozr%10)<=4:
        l=str(vozr)+' godA'
    else:
        l=str(vozr)+' let'
    pets[kl][vozr1]=l
    pets[kl][vid1]=vid
    pets[kl][xoz1]=xoz

    c=input('z-zakn4it, d-dalee ')



for key in pets:
    print(f"Eto {pets[key]['vid']} po kli4ke {key}. Vozrast {pets[key]['vozrast']}. Ima xozaina {pets[key]['xozain']}.")



