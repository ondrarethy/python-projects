################################################################################
#
#
#        ██████╗ ███████╗████████╗██╗  ██╗██╗   ██╗
#        ██╔══██╗██╔════╝╚══██╔══╝██║  ██║╚██╗ ██╔╝
#        ██████╔╝█████╗     ██║   ███████║ ╚████╔╝
#        ██╔══██╗██╔══╝     ██║   ██╔══██║  ╚██╔╝
#        ██║  ██║███████╗   ██║   ██║  ██║   ██║
#        ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝
#
#    Celé vytvořeno a zkompletováno 18.06.2017
#       Začátek: 15:42
#       Konec: 21:36
#
#   Autor: Ondřej Rethy
#
#       CHANGELOG:
#                    v1-18.06.2017 - Funkční program
#                    v2-19.06.2017 - Komentáře, přehlednost kódu
#
################################################################################

import time
import sys

p = []
nazev = input("Zadejte název vystupniho souboru (pokud neexistuje bude vytvořen, pokud existuje bude přepsán): ")
vystup = open(nazev, "w")       #otevře vystupní soubor
vstup = "in1.txt"    #cesta k in1.txt

f = open(vstup)  #zapíšeme text do proměnné TEXT
text = f.read()
f.close()

f = open(vstup, "w")  #na zacatek dame START, pak puvodni TEXT, pak END
f.write("START\n")
f.write(text)
f.write("\nEND")
f.close()

f = open(vstup)

radky = f.readline()   #čteme řádky a přidáváme postupně do pole
while radky != "END":
    radky = f.readline()
    p.append(radky)
f.close()

f = open("in1.txt", "w")     #prepisujeme opět na jenom TEXT
f.write(text)
f.close()

p = list(map(lambda x: str.replace(x, "\n", ""), p))    #odstrani \n   (zdroj. StackOverFlow)
p = list(map(lambda x: str.replace(x, " ", "*"), p))    #zmena " " na "."   (zdroj. StackOverFlow)
p = [x for x in p if x]                 #odstrani prazdne elementy v listu  (zdroj. StackOverFlow)
p.pop(-1)

for x in p:                 #hleda prvni vetu
    p1 = x
    p1 = p1[0:10]           #pouze prvnich 10 znaku
    for y in p:
        p2 = y
        p2 = p2[::-1]       #pouze poslednich 10 znaku
        p2 = p2[0:10]
        p2 = p2[::-1]
        if(p1 == p2):       #SHODA, jdeme dal
            break
    if(p1 != p2):           #nenašlo to navazující  část
        zacatek_raw = x     #první věta, neupravená
        x = x.replace("*", " ")
        zacatek = x
        break  
index1 = p.index(zacatek_raw)
p.pop(index1)
p.insert(0, zacatek_raw)  
for x in p:                 #hleda posledni vetu
    p1 = x
    p1 = p1[::-1]           #pouze poslednich 10 znaku
    p1 = p1[0:10]
    p1 = p1[::-1]
    for y in p:
        p2 = y
        p2 = p2[0:10]       #pouze prvnich 10 znaku
        if(p1 == p2):       #SHODA, jdeme dal
            break
    if(p1 != p2):           #nenašlo to pokračování
        konec_raw = x       #konecna veta, neupravená
        break
p2 = zacatek_raw            #neupraveny zacatek do P2
p2 = p2[::-1]
p2 = p2[0:10]               #pouze poslednich 10 znaku
p2 = p2[::-1]
vysledek = zacatek_raw      #zapise do vysledku prvni větu
END = 1                     #nastavi promenou na 1
while END != 0:
    for y in p:             #hleda pokracovani
        p1 = y
        p1 = p1[0:10]
        if(p1 == p2):       #našlo
            p2 = y
            p2 = p2[::-1]
            p2 = p2[0:10]   #upravi vetu na poslednich 10 znaku a opusti cyklus
            p2 = p2[::-1]
            break
    y = y.replace(p2, "")   #odebere spolecnou cast
    vysledek+= y            #prida k vysledku
    vysledek = vysledek.replace("*", " ")    #upravi (misto * budou opet mezery)
    konec = konec_raw
    konec = konec[::-1]
    konec = konec[0:10]     #poslednich 10 znaku konce
    konec = konec[::-1]
    if(p2 == konec):        #našla se posledni věta
        END = 0             #změnií na END a projistotu ukončí cyklus
        break
konec = konec.replace("*", " ")   #opět upraví konec
vysledek+=konec     #přidá konec na konec vysledku
vysledek+="."       #přidá na konec tečku, protože v původním chybí
print("Soubur vypsán a uložen, zavírám program.")
vystup.write(vysledek)   #zapisuje do souboru
vystup.close()
time.sleep(2)    #čeká
sys.exit()   #končí
