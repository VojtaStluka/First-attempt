from __future__ import annotations
from collections import deque

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
        
    def jak_daleko(self,jmeno1,jmeno2) -> None:
        if jmeno1 == jmeno2:
            return 0  # Pokud jsou to stejní lidé, vzdálenost je 0
        
        # Fronta pro BFS, každá položka bude obsahovat (uživatel, vzdálenost), prohledá vždy šířku jedné vrstvy známostí
        queue = deque([(self._users[jmeno1], 0)])  #list jména a vzdálenosti
        # Množina pro návštěvu (abychom se nevraceli zpět na již navštívené uživatele)
        visited = set([name1]) #funkce set() vždy má ve svém seznamu pouze jedinou konkrétní hodnotu
        
        while queue:
            current_user, distance = queue.popleft()    # z listu bude jménu pod proměnnou current_user a vzdálenost v distance
            
            # Procházení všech známých uživatelů
            for neighbor in current_user.znamost:
                if neighbor.jmeno == jmeno2:
                    return distance + 1      # Našli jsme jméno name2, vrátíme vzdálenost, tzn. přímo přítel; fronta je tímto prázdná
                if neighbor.jmeno not in visited: # Jestliže není v seznamu již prošlých lidí
                    visited.add(neighbor.jmeno) #Přidáme
                    queue.append((neighbor, distance + 1)) #Vrátíme zpět do fronty, čili cyklus se opakuje a máme vzdálenost >1
        
        return None  # Pokud jsme nenašli propojení

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

#Zkouška funkčnosti
vzdalenost = fb.jak_daleko("Adam", "Dana")
print(vzdalenost) 
