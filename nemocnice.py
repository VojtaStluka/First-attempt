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
