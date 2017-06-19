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
#    Celé vytvořeno a zkompletováno dne 08.06.2017
#       Začátek: 11:50
#       Konec: 12:30
#
#   Autor: Ondřej Rethy
#
#       CHANGELOG:
#                    v1-18.06.2017 - Funkční program (přepis do el. podoby)
#
################################################################################
sklad = {}
nazev = input("Zadej nazev souboru: ")
soubor = open(nazev)
radek = soubor.readline()
vydano = open('vydano.txt', 'a')
nevydano = open('nevydano.txt', 'a')
def zustatek_skladu(polozka, pocet):
    sklad_pocet = sklad[polozka]
    if int(sklad_pocet) >= int(pocet):
        return pocet
    elif sklad_pocet == 0:
        return 0
    else:
        deficit = int(pocet) - int(sklad_pocet)
        return deficit
while radek != "...":
    radek = soubor.readline()
    kousky = radek.split()
    if kousky[0] == "P":
        sklad[kousky[1]] = kousky[2]
        print("Přijato ", kousky[2], "x", kousky[1], ".")
    elif kousky[0] == "V":
        if int(sklad[kousky[1]]) >= int(kousky[2]):
            vydano.write(radek)
            print("Vydano ", kousky[2], "x", kousky[1], ".")
            zustatek = int(sklad[kousky[1]]) - int(kousky[2])
            sklad[kousky[1]] = zustatek
        elif int(sklad[kousky[1]]) == 0:
            nevydano.write(radek)
            print("Nevydano ", kousky[2], "x", kousky[1], ".")
        else:
            deficit = zustatek_skladu(kousky[1], kousky[2])
            vydam = int(kousky[2]) - int(deficit)
            print("Nevydano ", deficit, "x", kousky[1], ".")
            print("Vydano ", vydam, "x", kousky[1], ".")
            vydano.write("W.I.P.")
            nevydano.write("W.I.P.")
    else:
        print("ERROR")
print(sklad)
soubor.close
vydano.close
nevydano.close
