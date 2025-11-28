import string
karakterlanc = ""

# fájlbeolvasás
try:
    with open("string_input.txt",encoding = 'utf-8')as fajl:
        karakterlanc = fajl.read()
        #print(szoveg)
except IOError as ex:
    print(ex)

# 1.feladat
karakterlanc = karakterlanc.strip()    
# ================================================================    
    
# 2. feladat    
db_szam = 0
string.digits

for karakter in karakterlanc:
    if (karakter in string.digits):    
        db_szam += 1
        
print(db_szam)        
# ================================================================

