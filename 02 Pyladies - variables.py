#01
strana = 2852
povrch = 6 * strana**2
objem = strana **3

print("Povrch krychle je", povrch, "cm3")
print("Objem krychle je", objem, "cm3")

#02
strana = int(input("Zadej délku strany: "))
povrch = 6 * strana**2
objem = strana **3

print("Povrch krychle je", povrch, "cm3")
print("Objem krychle je", objem, "cm3")

#03
vice_jablek = False
jablka_cervena = True
ovoce_v_lednici = True

#04
heslo = input("Zadej heslo: ")

if heslo == "Tajné heslo":
    print("V pátek jsem viděla černého havrana.")
else:
    print("Smolíček.")

#05
vek = int(input("Zadej tvůj věk: "))
vaha = int(input("Zadej svou váhu: "))

if vek < vaha:
    print("Tvůj věk je menší než váha - hrůza!")
else:
    print("Vše v pořádku.")

#06
tah_pocitace = "kámen" 
tah_cloveka = str(input("Zadej svůj tah: "))

if tah_cloveka == "kámen":
    print("Plichta")
elif tah_cloveka == "nůžky":
    print("Počítač vyhrál")
elif tah_cloveka == "papír":
    print("Vyhrála jsi!")

tah_pocitace = "nůžky"
tah_cloveka = str(input("Zadej svůj tah: "))

if tah_cloveka == "kámen":
    print("Vyhrála jsi!")
elif tah_cloveka == "nůžky":
    print("Plichta")
elif tah_cloveka == "papír":
    print("Počítač vyhrál")

tah_pocitace = "papír"
tah_cloveka = str(input("Zadej svůj tah: "))

if tah_cloveka == "kámen":
    print("Počítač vyhrál")
elif tah_cloveka == "nůžky":
    print("Vyhrála jsi!")
elif tah_cloveka == "papír":
    print("Plichta")

#07
# První kolo
tah_pocitace = "kámen"
tah_cloveka = input("Zadej svůj tah (kámen, nůžky, papír): ")

if tah_cloveka == tah_pocitace:
    print("Plichta.")
elif (tah_cloveka == "kámen" and tah_pocitace == "nůžky") or \
     (tah_cloveka == "nůžky" and tah_pocitace == "papír") or \
     (tah_cloveka == "papír" and tah_pocitace == "kámen"):
    print("Vyhrála jsi!")
else:
    print("Počítač vyhrál.")

# Druhé kolo
tah_pocitace = "nůžky"
tah_cloveka = input("Zadej svůj tah (kámen, nůžky, papír): ")

if tah_cloveka == tah_pocitace:
    print("Plichta.")
elif (tah_cloveka == "kámen" and tah_pocitace == "nůžky") or \
     (tah_cloveka == "nůžky" and tah_pocitace == "papír") or \
     (tah_cloveka == "papír" and tah_pocitace == "kámen"):
    print("Vyhrála jsi!")
else:
    print("Počítač vyhrál.")

# Třetí kolo
tah_pocitace = "papír"
tah_cloveka = input("Zadej svůj tah (kámen, nůžky, papír): ")

if tah_cloveka == tah_pocitace:
    print("Plichta.")
elif (tah_cloveka == "kámen" and tah_pocitace == "nůžky") or \
     (tah_cloveka == "nůžky" and tah_pocitace == "papír") or \
     (tah_cloveka == "papír" and tah_pocitace == "kámen"):
    print("Vyhrála jsi!")
else:
    print("Počítač vyhrál.")


 