# 0
zvirata = ["pes",
           "kočka",
           "králík",
           "had"

]


def zjistit(zvirata, slovo):
    if slovo in zvirata:
        return True
    else:
        return False
slovo = input("Zadej slovo:")
print(zjistit(zvirata, slovo))

# 1
zvirata = ["pes",
           "kočka",
           "králík",
           "had"

]


def zjisti_kratke(zvirata):
    kratka_zvirata = []
    for zvire in zvirata:
        if len(zvire) < 5:
            kratka_zvirata.append(zvire)
    return kratka_zvirata
print(zjisti_kratke(zvirata))

# 2
zvirata = ["pes",
           "kočka",
           "králík",
           "had"

]

def kacka(zvirata):
    zvirata_kacka = []
    for zvire in zvirata:
        if zvire[0] == "k":
            zvirata_kacka.append(zvire)
    return(zvirata_kacka)
print(kacka(zvirata))

# 3
zvirata = ["pes",
           "kočka",
           "králík",
           "had"
]

def abeceda(zvirata):
    zvirata_abeceda = sorted(zvirata)
    return zvirata_abeceda
print(abeceda(zvirata))

# 4
zvirata1 = {"pes",
           "kočka",
           "králík",
           "had"
}

zvirata2 = {"želva", 
            "had", 
            "papoušek", 
            "anakonda", 
            "pes" 
}


def porovnej_seznamy(zvirata1, zvirata2):
    spolecna = []
    pouze_v_prvnim = []
    pouze_ve_druhem = []

    for zvire in zvirata1:
        if zvire in zvirata2:
            spolecna.append(zvire)
    
    for zvire in zvirata1:
        if zvire not in zvirata2:
            pouze_v_prvnim.append(zvire)
    
    for zvire in zvirata2:
        if zvire not in zvirata1:
            pouze_ve_druhem.append(zvire)

    return spolecna, pouze_v_prvnim, pouze_ve_druhem

# 5
def secti_dvojice(cisla):
    if len(cisla) == 2:
        return cisla[0] + cisla[1]
    else:
        return "Bohužel, umím sečíst jen dvě čísla."
print(secti_dvojice((3, 5)))


# 6
def serad_podle_abecedy(zvirata):
    dvojice = []
    for zvire in zvirata:
        klic = zvire[1:]  
        dvojice.append((klic, zvire))

    dvojice.sort()

    serazena_zvirata = []
    for klic, zvire in dvojice:
        serazena_zvirata.append(zvire)

    return serazena_zvirata

serazena_zvirata = serad_podle_abecedy(zvirata)
print(serazena_zvirata)