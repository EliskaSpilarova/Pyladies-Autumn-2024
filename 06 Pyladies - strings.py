# 0
def pohlavi(prijmeni):
    if prijmeni[-3:] == "ová":
        return "žena"
    else:
        return "muž"

prijmeni = (input("Napiš příjmení:"))
print("Jsem", pohlavi(prijmeni))

#1
def cisla_s_x(identifikacni_cislo):
    nahrazene_cislo = "x" * (len(identifikacni_cislo) - 4) + identifikacni_cislo[-4:] 
    return nahrazene_cislo

identifikacni_cislo = input("Zadej číslo:")
print(cisla_s_x(identifikacni_cislo))

#2
text = """
Netvař se tak na mě, že jsi úplně zlá
Jsou rána, kdy to nekončí
Na stole zbylo trochu v láhvi vína
Sklenici dolejvám
"""
enka = (text.lower().count("n"))
print(enka)

#3
def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka).strip().lower()
        if odpoved == "ano" or odpoved == "a":
            return True
        elif odpoved == "ne" or odpoved == "n":
            return False
        else:
            print("Nerozumím! Odpověz 'ano' nebo 'ne'.")

if ano_nebo_ne("Chceš si zahrát hru? "):
    print("OK! Ale napřed si ji musíš naprogramovat.")
else:
    print("Škoda.")

#4
def suda(cislo):
    if int(cislo) % 2 == 0:
        return True
    else:
        return False

cislo = (input("Zadej číslo:"))
print(suda(cislo))

# 5
def soucet(prvni_cislo, druhe_cislo, treti_cislo):
    if prvni_cislo + druhe_cislo + treti_cislo > 10:
        return True
    else:
        return False

prvni_cislo = int(input("Zadej první číslo:"))
druhe_cislo = int(input("Zadej druhé číslo:"))
treti_cislo = int(input("Zadej třetí číslo:"))

print(soucet(prvni_cislo, druhe_cislo, treti_cislo))

# 6
def bum_bac():
    for cislo in range (1, 101):
        if cislo % 3 == 0 and cislo % 5 == 0:
            print("bum-bác")
        elif cislo % 3 == 0:
            print("bum")
        elif cislo % 5 == 0:
            print("bác")
        else:
            print(cislo)

bum_bac()

#7
def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"
    
# 8
def tah(pole, cislo_policka, symbol):
    leva_cast = pole[:cislo_policka]  
    prava_cast = pole[cislo_policka+1:]  
    nove_pole = leva_cast + symbol + prava_cast
    return nove_pole

#9
def tah_hrace(pole):
    while True:
        vstup = input("Na kterou pozici chceš hrát? Zadej číslo od 0 do {}: ".format(len(pole) - 1))
        
        if not vstup.isdigit():
            print("To není platné číslo. Zkus to znovu.")
            continue

        cislo_policka = int(vstup)

        if cislo_policka < 0 or cislo_policka >= len(pole):
            print("Toto číslo je mimo rozsah herního pole. Zkus to znovu.")
            continue

        if pole[cislo_policka] != "-":
            print("Toto políčko je již obsazené. Zkus to znovu.")
            continue

        return tah(pole, cislo_policka, "x")