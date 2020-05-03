import random
import sys
import numpy as np

##EX1


# commandlineban ez volt: “L:” “White” “Black” “Red” “L:” “Red” “Green”
# lista = []
# for i in (sys.argv):
#     lista.append(i)
#
# lista1=[]
# lista2=[]
# flag=0
#
# for i in lista:
#     if 'L' in i:
#         flag+=1
#         continue
#     if flag==1:
#         lista1.append(i)
#     if flag==2:
#         lista2.append(i)
# print(np.sort(set(lista1)-set(lista2)))

##EX2

# osszeg=0
# osszeadas=''
# for i in range (1,int(sys.argv[1])+1):
#     if i<int(sys.argv[1]):
#         osszeg+=i
#         osszeadas+=str(i)+'+'
#     else:
#         osszeg+=i
#         osszeadas+=str(i)
#
#
# print(f'{osszeadas}={osszeg}')

##EX3

# szam=int(sys.argv[1])
# nap=(szam//(3600*24))
# ora=(szam-(nap*(3600*24)))//3600
# perc=(szam-(nap*3600*24)-(ora*3600))//60
# mp=(szam-(nap*3600*24)-(ora*3600))%60
#
#
# print(f' {szam} masodperc {nap} nap, {ora} ora, {perc} perc es {mp} masodperc.')

##EX4

def karakterKereso(sztring,karakter):
    db=0
    for i in sztring:
        if i == karakter:
            db+=1
        else:
            continue
    return db

print(karakterKereso((sys.argv[1]),'a'))

##EX5

# def randomszam(n, output):
#     for i in range (int(n)):
#         print(random.randint(1,101),file = output)
#
# def osszeadas(output):
#     osszeg=0
#     for i in output:
#         osszeg+=int(i)
#     return osszeg
#
# n=sys.argv[1]
# ki = open(sys.argv[2],'w+')
# randomszam(n,ki)
# ki.seek(0)
# print(osszeadas(ki))


