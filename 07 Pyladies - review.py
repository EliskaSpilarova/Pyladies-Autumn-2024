# 0
import random

def tah_pocitace(pole):
    while True:
        pozice = random.randint(0, len(pole) - 1)  
        if pole[pozice] == "-":  #
            return tah(pole, pozice, "o")  

# 1
def piskvorky1d():
    pole = "--------------------"
    while True:
        pole = tah_hrace(pole)
        print("Po tahu hráče:", pole)

        vysledek = vyhodnot(pole)
        if vysledek != "-":
            break

        pole = tah_pocitace(pole)
        print("Po tahu počítače:", pole)

        vysledek = vyhodnot(pole)
        if vysledek != "-":
            break

    if vysledek == "x":
        print("Vyhrál jsi!")
    elif vysledek == "o":
        print("Prohrál jsi!")
    else:
        print("Remíza!")

piskvorky1d()

# 4
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

for i in range(10):
    print(fibonacci(i))

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def show_whole_example(n):
    result = "1"
    if n <= 0:
        return result
    for i in range(1, n + 1):
        result += f" × {i}"
    return result

for i in range(10):
    print(i, factorial(i), sep=":", end=" ")
    print(f"({show_whole_example(i)})")