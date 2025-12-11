#FÁJLBEOLVASÁS
#====================================================================
lista = []
try:
    with open("input.txt",encoding = 'utf-8') as fajl:
        lista = fajl.read()
except IOError as hiba:
    print(hiba)
#====================================================================
#print(lista)
    
# 1. FELADAT:
def feladat_1():

    szoveg_szelet = lista.strip().split('\n')            
    karakterhossz = 0

    for lista in szoveg_szelet:
        karakterhossz += len(lista)
    return karakterhossz

#print(len(lista))

def feladat_1_2():
    szavak = lista.split(' ')
    return len(szavak)

try:
    with open("output.txt",'w',encoding = 'utf-8') as fajl:
        fajl.write(f"1. feladat: \n {feladat_1}")
        fajl.write(f"1_2.feladat: \n {feladat_1_2} ")
except IOError as hiba:
    print(hiba)


#====================================================================
print(f"1. feladat: \n  Számold meg és írd ki az output.txt elejére a szövegben található KARAKTEREK és SZAVAK teljes számát. Karekterek száma: {feladat_1} \n ")





#====================================================================    