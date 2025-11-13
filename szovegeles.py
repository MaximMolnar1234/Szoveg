szoveg=""
try:
    with open("scifi_input_v2.txt", encoding="utf-8") as forras:
        szoveg = forras.read()
except IOError as hiba:
            print(hiba)
    
# 1.feladat
lista = szoveg.split("**")
print(szoveg.split("**"))

for i in range(len(lista)):
    lista[i] = lista[i].strip()
"""
for sor in lista:
    if (len(sor) == 0):
        lista.remove(sor)
"""
db = 0
for i in range(len(lista)):
    if (len(lista[i]) > 0):
        lista[db] = lista[i] 
        db += 1
for i in range(db, len(lista)):
    lista.pop()    


print(lista)    
    

    