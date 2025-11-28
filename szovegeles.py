szoveg = ""
try:
    with open("scifi_input_v2.txt",encoding = 'utf-8')as fajl:
        szoveg = fajl.read()
        #print(szoveg)
except IOError as ex:
    print(ex)

def feladat1():
    
    lista=szoveg.strip().split('**')
    for i in range (len(lista)):
        lista[i]=lista[i].strip()
    db = 0
    for i in range (len(lista)):
        if (len(lista[i]) > 0):
            lista[db] = lista[i]
            db += 1
    for i in range(db,len(lista)):
        lista.pop()
    
    for sz in lista:
        kiir += sz + "\n"
    
    
    return kiir

try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        for elem in lista4:
            fajl.write(feladat1())
            #fajl.write(feladat2())
            #fajl.write(feladat3())
            #fajl.write(feladat4())
            #fajl.write(feladat5())
            #fajl.write(feladat6())
            #fajl.write(feladat7())         


except IOError as ex:
    print(ex)









    
# 1. feladat:
lista=szoveg.strip().split('**')
for i in range (len(lista)):
    lista[i]=lista[i].strip()
"""for sor in lista:
    if (len(sor)==0):
        lista.remove(sor)
"""
db = 0
for i in range (len(lista)):
    if (len(lista[i]) > 0):
        lista[db] = lista[i]
        db += 1
for i in range(db,len(lista)):
    lista.pop()
#print(lista)

# 2. feladat:
for i in range(len(lista)):
    lista[i]=lista[i].lower()

#print(lista)    

for i in range(0, len(lista), 2):
    lista2 = lista[i].split(' ')
    lista2[0] = lista2[0].upper()
    #lista[i] = lista2[0] + lista2[1]  
    szo = " "
    for j in range(len(lista2)):
        szo += lista2[j] + " "   
    lista[i] = szo.strip()    
print(lista)

try:
    with open("scifi_output.txt","w",encoding = 'utf-8')as fajl:
         for i in lista:
             fajl.write(i + "\n") 
        #print(szoveg)
except IOError as ex:
    print(ex)

# 3. feladat:
szoveg = szoveg.replace (',' ,'').replace ('.','').replace ('*','')
print(szoveg)
lista3 = szoveg.strip().split(' ')

print(lista3)    

try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
         fajl.write (str(len(lista3))+"\n") 
except IOError as ex:
    print(ex)

# 4. feladat:
lista4 = []

for elem in lista3:
    if (elem.lower().endswith("és") and elem not in lista4):
        lista4.append(elem)

print(lista4)        
print()        
try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        for elem in lista4:
            fajl.write(elem + "\n")         
except IOError as ex:
    print(ex)

# 5. feladat:
lista5 = []

for elem in lista3:
    if (elem.lower().startswith("a") and (elem.lower() != "a" and  elem.lower() != "az")):
        lista5.append(elem)

print(len(lista5))
print()
# 6. feladat:
try:
    with open("scifi_output.txt","a",encoding = 'utf-8')as fajl:
        for elem in lista4:
            fajl.write(str(szoveg.find("jövőben")) + "\n")         
except IOError as ex:
    print(ex)

# 7. feladat:
lista5 = []

for elem in lista3:
    elem = elem.lower()
    if (len(elem) >= 10 and elem not in lista5 ):
        lista5.append(elem)
lista5.sort()
print(lista5)

try:
    with open("output.txt","w",encoding = 'utf-8')as fajl:
        for elem in lista5:
            fajl.write(elem + "\n")         
except IOError as ex:
    print(ex)

print("FELADAT VÉGE")
