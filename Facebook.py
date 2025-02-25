from __future__ import annotations
from dataclasses import dataclass

class Uzivatel:
    def __init__(self,jmeno) -> None:
        self.jmeno:str = jmeno
        self.znamost:list[Uzivatel] = []

class Facebook:
    def __init__(self) -> None:
        self._users: dict [str,Uzivatel]={}

    def pridej_uzivatel(self,jmeno:str) -> None:
        self._users[jmeno] = Uzivatel(jmeno)

    def pridej_znamost(self,jmeno1,jmeno2) -> None:
        user1_uzel=self._users[jmeno1]
        user2_uzel=self._users[jmeno2]
        user1_uzel.znamost.append(user2_uzel)
        user2_uzel.znamost.append(user1_uzel)
        
    def jak_daleko(name1, name2) -> None:
        ...

# Vytvoření instance Facebooku
fb = Facebook()

# Seznam unikátních jmen
jmena = ["Adam", "Beata", "Cyril", "Dana", "Emil", "František", "Gabriela", "Hana", "Ivan", "Jana",
    "Karel", "Lenka", "Marek", "Nina", "Ondřej", "Petra", "Quentin", "Radka", "Stanislav", "Tereza",
    "Urbán", "Veronika", "Walter", "Xenie", "Yvona", "Zdeněk", "Alex", "Blanka", "Cecilie", "David"]

# Vkládání známostí do Facebooku
for jmeno in jmena:
    fb.pridej_uzivatel(jmeno)
  
# Hardkodované známosti
znamosti = [("Adam", "Beata"), ("Adam", "Cyril"), ("Beata", "Dana"),
    ("Cyril", "Emil"), ("Cyril", "František"), ("Dana", "Gabriela"),
    ("Emil", "Hana"), ("František", "Ivan"), ("Gabriela", "Jana"),
    ("Hana", "Karel"), ("Ivan", "Lenka"), ("Jana", "Marek"),
    ("Karel", "Nina"), ("Lenka", "Ondřej"), ("Marek", "Petra"),
    ("Nina", "Quentin"), ("Ondřej", "Radka"), ("Petra", "Stanislav"),
    ("Quentin", "Tereza"), ("Radka", "Urbán"), ("Stanislav", "Veronika"),
    ("Tereza", "Walter"), ("Urbán", "Xenie"), ("Veronika", "Yvona"),
    ("Walter", "Zdeněk"), ("Xenie", "Alex"), ("Yvona", "Blanka"),
    ("Zdeněk", "Cecilie"), ("Alex", "David"), ("Blanka", "Adam")]

# Vkládání známostí do Facebooku
for clovek1, clovek2 in znamosti:
    fb.pridej_znamost(clovek1, clovek2)
