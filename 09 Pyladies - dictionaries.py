# 0
def umocni(n):
    mocniny = {}
    for i in range (1, n + 1):
        mocniny[i] = i ** 2
    return mocniny
print(umocni(5))

# 1
def soucet_klicu_a_hodnot(slovnik):
    suma_klicu = sum(slovnik.keys())
    suma_hodnot = sum(slovnik.values())
    return (suma_klicu, suma_hodnot)

# 2
def pocet_znaku(retezec):
    vysledny_slovnik = {}
    for znak in retezec:
        if znak in vysledny_slovnik:
            vysledny_slovnik[znak] += 1
        else:
            vysledny_slovnik[znak] = 1
    return vysledny_slovnik
  
  {'M': 1, 'á': 2, 'm': 1, 'e': 2, ' ': 2, 'r': 1, 'd': 2, 'i': 2, 'P': 1, 'y': 1, 'L': 1, 'a': 1, 's': 1, '!': 1}


