# 0
class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

# 1
class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()

# 2
class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()

    def kdo_jsi(self):
       return f"Jmenuji se {self.jmeno} {self.prijmeni}"

# 3
class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno.capitalize()
        self.prijmeni = prijmeni.capitalize()
        self.inicialy = self.jmeno[0].upper() + self.prijmeni[0].upper()

    def kdo_jsi(self):
        return f"Jmenuji se {self.jmeno} {self.prijmeni} a mé iniciály jsou {self.inicialy}"