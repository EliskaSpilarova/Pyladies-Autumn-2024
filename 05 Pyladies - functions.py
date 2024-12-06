#0
def pocet_vterin(cas_v_minutach, cas_ve_vterinach):
    return(cas_v_minutach * 60) + cas_ve_vterinach
   
print(pocet_vterin(2,30))

#1
def max_hodnota(cislo_jedna, cislo_dva, cislo_tri):
    if cislo_jedna >= cislo_dva and cislo_jedna >= cislo_tri:
        return(cislo_jedna)
    elif cislo_dva >= cislo_jedna and cislo_dva >= cislo_tri:
        return(cislo_dva)
    else:
        return(cislo_tri)

#2
def kocky_BMI(obvod_hrudniku, zadni_noha):
    return((obvod_hrudniku / 0.7062 - zadni_noha) / 0.9156) - zadni_noha

print(kocky_BMI(50,5))

#3
import turtle

def nakresli_n_uhelnik(n):
    uhel = 180 * (1 - 2 / n)  
    delka_strany = 200 / n  

    for i in range(n):
        turtle.forward(delka_strany) 
        turtle.left(180 - uhel)  

for pocet_stran in [5, 6, 7, 8]:
    nakresli_n_uhelnik(pocet_stran)
    turtle.penup()
    turtle.forward(150)  
    turtle.pendown()

#4
def obrazec():
    for radek in range(6):              
        for sloupec in range(6):        
            if radek == 0 or radek == 5 or sloupec == 0 or sloupec == 5:
                print("X", end=" ")     
            else:
                print(" ", end=" ")     
        print()                         

obrazec()

#5
import random
from random import randrange

vitez = 0
max_hodu = 0

def hazej_kostkou():
    pokusy = 0
    while True:
        hod = randrange(1, 7)
        pokusy += 1
        print("Hodil:", hod)
        if hod == 6:
            return pokusy  

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

#6
def bum_bac (cislo):
    if cislo % 2 == 0:
        return "bác" 
    else:
        return "bum"
print(bum_bac(7))

#7
def bum_bac (cislo):
    if cislo % 2 == 0:
        return "bác" 
    else:
        return "bum"

def vypis_bum_bac(n):
    for i in range(1, n + 1):
       print(bum_bac(i))

vypis_bum_bac(6)