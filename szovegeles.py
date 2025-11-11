szoveg=""
try:
    with open("scifi_input_v2.txt", encoding="utf-8") as forras:
        szoveg = forras.read()
except IOError as hiba:
            print(hiba)
    
    