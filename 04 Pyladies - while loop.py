#0
heslo = input("Zadej heslo: ")
while heslo != "pyladies":
    print("Špatně!")
    heslo = input("Zadej heslo: ")

print("Správně!")

#1
while True:
    tah_pocitace = "kámen"
    tah_cloveka = input("Zadej svůj tah (kámen, nůžky, papír, nebo konec): ")

    if tah_cloveka == "konec":
        print("Neplecha ukončena.")
        break

    # print("Volba počítače:", tah_pocitace)
    if tah_cloveka == tah_pocitace:
        print("Plichta.")
    elif tah_cloveka == "papír":
        print("Vyhrála jsi!")
    elif tah_cloveka == "nůžky":
        print("Počítač vyhrál.")

#2
from random import randrange

while True:
    cislo = randrange(3)
    if cislo == 0:
        tah_pocitace = "kámen"
    elif cislo == 1:
        tah_pocitace = "nůžky"
    elif cislo == 2:
        tah_pocitace = "papír"

    tah_cloveka = input("Zadej svůj tah (kámen, nůžky, papír, nebo konec): ")

    if tah_cloveka == "konec":
        print("Neplecha ukončena.")
        break

    
    if tah_cloveka == tah_pocitace:
        print("Plichta.")
    elif (tah_cloveka == "papír" and tah_pocitace == "kámen") or \
         (tah_cloveka == "kámen" and tah_pocitace == "nůžky") or \
         (tah_cloveka == "nůžky" and tah_pocitace == "papír"):
        print("Vyhrála jsi!")
    else:
        print("Počítač vyhrál.")

#3
cislo = int(input("Zadej náhodné číslo:"))
nejmensi_cislo = int(cislo)

while cislo != 0:
    if cislo < nejmensi_cislo:
        nejmensi_cislo = cislo
    print("Smolíček!")
    cislo = int(input("Zadej náhodné číslo:"))

print("Je to nula!")

print("Nejmenší číslo je", nejmensi_cislo)

#4
import random

vitez = 0
max_hodu = 0

for hrac in range(1, 5):
    pocet_hodu = 0
    
    while True:
        hod = random.randint(1, 6)
        pocet_hodu += 1
        print(f"Hráč {hrac} hodil: {hod}")
        
        if hod == 6:
            break

    if pocet_hodu > max_hodu:
        max_hodu = pocet_hodu
        vitez = hrac

print(f"Vyhrál hráč {vitez} s počtem hodů: {max_hodu}")

#5
cislo_1 = int(input("Zadej první číslo"))
cislo_2 = int(input("Zadej druhé číslo"))
operace = input("Vyber si jedno ze znamének +, -, * nebo /")

if operace == "+":
    vysledek = cislo_1 + cislo_2
elif operace == "-":
    vysledek = cislo_1 - cislo_2
elif operace == "*":
    vysledek = cislo_1 * cislo_2
elif operace == "/":
    vysledek = cislo_1 / cislo_2

print("Výsledek: ", vysledek)

#6
for i in range (4):
    if i == 0:
        print("první řádek")
    else:
        print("není první")


