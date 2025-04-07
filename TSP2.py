from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any
import heapq
from collections import deque

#velké TSP
@dataclass
class Mesto:
    nazev:str
    sousede: list[tuple[str,int]]

class Graph:
    
    def __init__(self) -> None:
        self.cities : dict[str,Mesto] = {}


    def kolik_mest(self):
        return len(self.cities)
        
    def _jednostrane_pridani_mesta(self, mesto_z: str, mesto_do: str, vzdalenost: int) -> None:
        if mesto_z not in self.cities:
            self.cities[mesto_z] = Mesto(mesto_z,[])

        self.cities[mesto_z].sousede.append((mesto_do,vzdalenost))
        
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        self._jednostrane_pridani_mesta(from_city, to_city, distance)
        self._jednostrane_pridani_mesta(to_city, from_city, distance)

    def najdi_sousedy(self,z_mesta):
        return self.cities[z_mesta].sousede

    def existuje_cesta(self, z_mesta, do_mesta) -> bool:
        return do_mesta in [soused[0] for soused in self.cities[z_mesta].sousede]



@dataclass
class Cesta:
    mesta: List[str]
    delka: int
    
    def pridej_mesto(self, dalsi_mesto, vzdalenost) -> Cesta:
        return Cesta(self.mesta+[dalsi_mesto],self.delka+vzdalenost)


reseni: list[Cesta] = []


def vyzkousej_cesty(graph, dosud_projita_cesta):
    global reseni
    sousedi=graph.najdi_sousedy(dosud_projita_cesta.mesta[-1])    
    for soused,vzdalenost in sousedi:
        if soused in dosud_projita_cesta.mesta:
            continue
        cesta_do_souseda=dosud_projita_cesta.pridej_mesto(soused, vzdalenost)
        if len(cesta_do_souseda.mesta)==graph.kolik_mest():
            if graph.existuje_cesta(soused,cesta_do_souseda.mesta[0]):
                print(f"nasel jsem reseni!: {cesta_do_souseda}")
                reseni.append(cesta_do_souseda)
        else:
            vyzkousej_cesty(graph, cesta_do_souseda)

#malé TSP

@dataclass
class City:
    name:str
    neighbors: List[Tuple[str, int]]  # list of (neighbor_name, distance)

class Graph:
    def __init__(self):
        self.cities: Dict[str, City] = {}

    def add_edge(self, from_city: str, to_city: str, distance: int):
        if from_city not in self.cities:
            self.cities[from_city] = City(from_city, [])
        if to_city not in self.cities:
            self.cities[to_city] = City(to_city, [])

        self.cities[from_city].neighbors.append((to_city, distance))
        self.cities[to_city].neighbors.append((from_city, distance))  # undirected

    def get_neighbors(self, city_name: str) -> List[Tuple[str, int]]:
        return self.cities[city_name].neighbors
    
    def total_cities(self):
        return len(self.cities)
    
    def path_exists(self, from_city: str, to_city: str) -> bool:
        for neighbor, _ in self.get_neighbors(from_city):
            if neighbor == to_city:
                return True
        return False

class Path:
    def __init__(self, visited: List[str], total_distance: int):
        self.visited = visited
        self.total_distance = total_distance

    def extend(self, next_city: str, distance: int) -> 'Path':
        return Path(self.visited + [next_city], self.total_distance + distance)


#Chatovo TSP
def dijkstra(graph, start):
    # Create a priority queue to store the nodes and their tentative distances
    pq = [(0, start)]  # (distance, node)
    
    # Create a dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current distance is greater than the recorded distance, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Explore each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

#binární halda
@dataclass
class Element:
    value: Any
    priority: int
 
class BinaryHeap:

    def __init__(self):
        self.heap: list[Element] = []
        
    def push(self,element:Element):
        self.heap.append(element)
        idx=(len(self.heap))-1
        while idx>0:
            idx_rodic = (idx-1) // 2
            rodic = self.heap[idx_rodic] 
            dite = element           
            if rodic.priority > dite.priority:
                self.heap[idx] = rodic
                self.heap[idx_rodic] = dite
            else: 
                break
         

    def pop(self):
        min_element=self.heap[0]
        last_element=self.heap.pop()    #najdeme poslední prvek
        if not self.heap: #Pokud jsme odstranili poslední prvek, vrátíme rovnou
            return min_element
        else:
            self.heap[0]=last_element   #prohodíme do kořene
            idx=0

            while True:
                smallest=idx
                left_child = 2 * idx + 1
                right_child = 2 * idx + 2
                if left_child <= len(self.heap)-1 and self.heap[left_child].priority < self.heap[smallest].priority:    #kontrola min_heap a zároveň kontrola, jestli existuje (v poslední vrstvě být nutně nemusí)
                        smallest = left_child
                if  right_child <= len(self.heap)-1 and self.heap[right_child].priority < self.heap[smallest].priority:
                        smallest = right_child
                if smallest != idx:
                    self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]   #prohození ve vrstvách
                    idx = smallest
                else: 
                    break
            return min_element


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        min_idx = 0
        return self.heap[min_idx]



#Lukášova binární halda
from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, element):
        self.heap.append(element)
        current_index = len(self.heap) - 1
        
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.heap[parent_index].priority > self.heap[current_index].priority:
                self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
                current_index = parent_index
            else:
                break

    def pop(self):
        if not self.heap:
            return None
        
        min_element = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            index = 0
            while True:
                smallest = index
                left = 2 * index + 1
                right = 2 * index + 2
                
                if left < len(self.heap) and self.heap[left].priority < self.heap[smallest].priority:
                    smallest = left
                
                if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
                    smallest = right
                
                if smallest == index:
                    break
                
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
        
        return min_element


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        # vrati nejmensi element ve fronte (element na cele fronty)
        # protoze mame naivni implementaci, musime projit cely seznam
        min_idx = 0
        for idx in range(1,len(self.heap)):
            if self.heap[idx].priority < self.heap[min_idx].priority:
                min_idx = idx
        return self.heap[min_idx]
      


#Facebook

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
        
        # Fronta pro BFS, každá položka bude obsahovat (uživatel, vzdálenost), prohledá vždy do šířky jednu vrstvy známostí
        fronta = deque([(self._users[jmeno1], 0)])  #list jména a vzdálenosti
        # Množina pro návštěvu (abychom se nevraceli zpět na již navštívené uživatele)
        visited = set([jmeno1]) #funkce .set() obsahuje vždy jedinou konkrétní hodnotu
        
        while fronta:
            current_user, distance = fronta.popleft()    # z listu bude jménu pod proměnnou current_user a vzdálenost v distance
            for soused in current_user.znamost:     # Procházení všech známých uživatelů
                if soused.jmeno == jmeno2:
                    return distance + 1      # Našli jsme jméno name2, vrátíme vzdálenost, tzn. přímo přítel; fronta je tímto prázdná
                if soused.jmeno not in visited: # Jestliže není v seznamu již prošlých lidí
                    visited.add(soused.jmeno) #Přidáme
                    fronta.append((soused, distance + 1)) #Vrátíme zpět do fronty, čili cyklus se opakuje a máme vzdálenost >1     
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
vzdalenost = fb.jak_daleko("Adam", "Cecilie")
print(vzdalenost) 




