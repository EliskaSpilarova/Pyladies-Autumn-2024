#00
zprava = "Řádek"
for cislo in range(5):
    print(zprava, cislo)

#01
for cislo in range (1,12,2):
    print(cislo)

#02
for cislo in range (1, 5):
    mocnina = cislo ** 2
    print(cislo, "na druhou je", mocnina)
   
#03
for radek in range(5):
    for sloupec in range(5):
        print("x", end = " ")
    print()

#04
for radek in range(1,5):
    for sloupec in range(1,5):
        print(radek * sloupec, end = " ")
    print()

#05
for radek in range(1, 5):
    for sloupec in range(radek):
        print("x", end = " ")
    print()

#06
from turtle import forward, left, exitonclick, right
delka = 100
for strana in range(3):
    forward(delka)
    left(120)

exitonclick()

#07
import math
from math import sqrt, degrees
from turtle import forward, left, exitonclick, right, penup, pendown

delka = 100

for strana in range(4):
    forward(delka)
    left(90)

left(45)
forward((math.sqrt(2)*delka)) 
left(135)
penup()
forward(delka)
left(135)
pendown()
forward((math.sqrt(2)*delka))
penup()

left(135)
penup()
forward(delka)
pendown()
left(45)
forward((math.sqrt(2)*delka/2))
left(90)
forward((math.sqrt(2)*delka/2))



exitonclick()

#08
from turtle import exitonclick, forward, left

neznama = int(input("Zadej počet stran n_úhelníku")) 
 
uhel = 360 / neznama
strana = 200 / neznama

if neznama > 2:
    for n_uhelnik in range(neznama):
        forward(strana)
        left(uhel)
    

exitonclick()

