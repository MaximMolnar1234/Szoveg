import string

# 1. feladat
betu = ""

try:
    with open("string_input.txt",encoding = 'utf-8')as fajl:
        betu = fajl.read()
except IOError as ex:
    print(ex)

betu = betu.strip()
#=======================================================================
# 2. feladat
db_szam = 0
db_betu = 0

for i in  betu:
    if i in string.digits:
        db_szam += 1

for i in  betu:
    if i in string.ascii_letters:
        db_betu += 1

print (db_szam)
print (db_betu)
#========================================================================
# 3.feladat
lista = []

for i in betu:
    if (i in string.punctuation and i not in lista):
        lista.append(i)

try:
    with open("string_output.txt", "a" ,encoding = 'utf-8')as fajl:
        for i in range(len(lista)):
            
            if (i < len(lista)-1):
                fajl.write(lista[i] + ",")
            else:
                fajl.write(lista[i])    
except IOError as ex:
    print(ex)
#========================================================================
# 4.feladat
sorok = betu.split('\n')

szavak = []

for sor in sorok:
    sor_darabok = sor.split(' ')
    szavak.append(sor_darabok)


for szo in szavak:
    if ("A" or '5' or '3' or 'b' or '?') in szo:
        i = 0
        while i < len(szo) and szo[i] in string.hexdigits:
            i += 1
        if i == len(szo):
            print("Megtalált!",szo)  


