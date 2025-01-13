'''cache = {}
cache[0] = 0
cache[1] = 1

def Fibonacci(cislo):
    if cislo <= 1:
        return cislo
    # Podíváme se, zda už máme výsledek v cache
    if cislo in cache:
        return cache[cislo]
    else:
        # Pokud není v cache, vypočítáme a uložíme do cache
        print("Počítám z: " + str(cislo))
        cache[cislo] = Fibonacci(cislo - 1) + Fibonacci(cislo - 2)
        return cache[cislo]

cislo = int(input("Zadejte číslo: "))
print(Fibonacci(cislo))
'''


def Fibonacci(cislo):
    if cislo <= 1:
        return cislo
    else:
        male=Fibonacci(cislo - 1)
        mensi=Fibonacci(cislo - 2)
        real_cislo = male + mensi
        return real_cislo

cislo = int(input("Zadejte číslo: "))
print(Fibonacci(cislo))

#datové modely vlastní nemocnice

from dataclasses import dataclass
from enum import Enum
from typing import List

class Specializace(Enum):
    KARDIOLOG = 0
    NEUROLOG = 1
    NEFROLOG = 2

@dataclass
class Lekar:
    jmeno: str
    specializace: Specializace

class Pacient:
    def __init__(self, rc: int, jmeno: str, pohlavi: bool, typ_pacienta: str):
        self.rc = rc 
        self.jmeno = jmeno
        self.pohlavi = pohlavi 
        self.typ_pacienta = typ_pacienta  

class Ordinace:
    def __init__(self, specializace: Specializace, hl_lekar: Lekar, pomoc_lekar: Lekar, pacienti: List[Pacient]):
        self.specializace = specializace
        self.hl_lekar = hl_lekar
        self.pomoc_lekar = pomoc_lekar
        self.pacienti = pacienti

class Nemocnice:
    def __init__(self, name: str):
        self.name = name
        self.ordinace = []

    def add_ordinace(self, ordinace: Ordinace):
        self.ordinace.append(ordinace)

lekar1 = Lekar("Karel Vins", Specializace.KARDIOLOG)
lekar2 = Lekar("Petr Skala", Specializace.NEFROLOG)
