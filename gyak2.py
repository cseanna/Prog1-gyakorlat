##EX1

while True:
    try:
        x = int(input('Adj meg egy szamot: '))
        print(x)
        break
    except ValueError:
        print('Nem jo erteket adtal meg.')

##EX2

try:
    konzolba = open('k','r')
    for i in konzolba:
        print(i,end='')
    konzolba.close()
except FileNotFoundError:
    print('A fajl nem talalhato.')

##EX3


def LannisterSzamlalo(fajl):
    szamlalo=0
    for sor in fajl:
        szavak = sor.split(' ')
        for szo in szavak:
            if 'Lannister' in szo:
                szamlalo+=1
    return szamlalo

reszlet = open('input','r')
try:
    print(LannisterSzamlalo(reszlet))
except FileNotFoundError:
    print('A fajl nem talalhato.')
reszlet.close()

##EX4

def betuCserelo(fajl):
    uj_reszlet=''
    for sor in fajl:
        for betu in sor:
            if 'A' <= betu <='Z':
                uj_reszlet += betu.lower()
            if 'a' <= betu <= 'z':
                uj_reszlet+= betu.upper()
            else:
                uj_reszlet+=betu
    out = open('output','w')
    print(uj_reszlet, file=out)
try:
   betuCserelo(open('input','r'))
except FileNotFoundError:
    print('A fajl nem talalhato.')

##EX5
import string

def leghosszabbSzo(fajl):

    max=0
    leghosszabb=''
    uj_szoveg = ''
    for sor in fajl:
        for karakter in sor:
             if karakter not in string.punctuation:
                uj_szoveg+=karakter
                uj_szoveg.split()
    szavak=uj_szoveg.split()
    for e in szavak:
        if len(e)>max:
            leghosszabb=''
            max=len(e)
            leghosszabb+=e+' '
        elif len(e)==max:
            leghosszabb+=e+' '


    print(f'A leghosszabb szo: {leghosszabb}\nKarakterek szama: {max}',file=output)

input = open('input','r')
output = open('outout','w')
leghosszabbSzo(input)
input.close()
output.close()