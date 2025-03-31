from typing import List, Tuple
from dataclasses import dataclass
from __future__ import annotations 


@dataclass
class Mesto:
    nazev:str
    sousede:list[tuple[str,int]]


class Graph:
    
    def __init__(self) -> None:
        self.cities : dict[str,Mesto] = {}

    def _jednostranne_pridani_mesta(self, from_city: str, to_city: str,distance: int):
            if from_city not in self.cities:
                self.cities[from_city]= Mesto(from_city,[])
            self.cities[from_city].sousede.append((to_city,distance))
    
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        self._jednostranne_pridani_mesta(from_city, to_city)
        if from_city not in self.cities:
            self.cities[from_city]= Mesto(from_city,[])
        self.cities[from_city].sousede.append((to_city,distance))
        self.cities[to_city].sousede.append((from_city,distance))
    
    def vrat_sousedy(self,z_mesta):
        return self.cities[z_mesta].sousede

    def kolik_mest(self):
        return len(self.cities)
    
@dataclass
class Cesta:
    mesta:List[str]
    delka:int
    def pridej_mesto(self,dalsi_mesto,vzdalenost) -> Cesta:
        return Cesta(self.mesta+[dalsi_mesto],self.delka+vzdalenost) #[] spojoje dva seznamy a tvoří jeden

reseni:list[Cesta]
def vyzkousej_cesty(graph,dosud_projitcesta:Cesta):
    global reseni
    sousedi=graph.vrat_sousedy(dosud_projitcesta[-1]) #vezme poslední prvek v seznamu díky zápornému indexu
    for soused,vzdalenost in sousedi:
        if soused in dosud_projitcesta.mesta:
            continue # už nebude pokračovat dál ve for cyklu
        cesta_do_souseda=dosud_projitcesta.pridej_mesto(soused, vzdalenost)
        if len(cesta_do_souseda.mesta)==graph.kolik_mest(): #může být kandidát na řešení?
            if graph.existuje_cesta(soused,cesta_do_souseda.mesta[0]):  #kontroluje, zda se můžeme vrátit do výchozího       
                    reseni.append(cesta_do_souseda)
        else: 
            vyzkousej_cesty(graph,cesta_do_souseda)
        

def load_europe() -> Graph:
    graph = Graph()
    graph.new_edge("Lisbon", "Madrid", 339)
    graph.new_edge("Naples", "Rome", 134)
    graph.new_edge("Hamburg", "Copenhagen", 180)
    graph.new_edge("Hamburg", "Berlin", 182)
    graph.new_edge("Berlin", "Warsaw", 345)
    graph.new_edge("Amsterdam", "Hamburg", 338)
    graph.new_edge("Amsterdam", "Brussels", 164)
    graph.new_edge("Berlin", "Prague", 219)
    graph.new_edge("Prague", "Warsaw", 479)
    graph.new_edge("Prague", "Vienna", 185)
    graph.new_edge("Munich", "Prague", 174)
    graph.new_edge("Vienna", "Warsaw", 464)
    graph.new_edge("Vienna", "Budapest", 214)
    graph.new_edge("Warsaw", "Budapest", 394)
    graph.new_edge("Budapest", "Belgrade", 319)
    graph.new_edge("Vienna", "Belgrade", 490)
    graph.new_edge("Budapest", "Trieste", 384)
    graph.new_edge("Trieste", "Vienna", 317)
    graph.new_edge("Trieste", "Belgrade", 403)
    graph.new_edge("Munich", "Vienna", 280)
    graph.new_edge("Munich", "Rome", 582)
    graph.new_edge("Genoa", "Trieste", 361)
    graph.new_edge("Genoa", "Rome", 328)
    graph.new_edge("Trieste", "Rome", 442)
    graph.new_edge("Paris", "Genoa", 629)
    graph.new_edge("Genoa", "Bern", 304)
    graph.new_edge("Genoa", "Brussels", 740)
    graph.new_edge("Bern", "Brussels", 497)
    graph.new_edge("Amsterdam", "Bern", 558)
    graph.new_edge("Amsterdam", "Munich", 526)
    graph.new_edge("Bern", "Munich", 311)
    graph.new_edge("Bern", "Trieste", 489)
    graph.new_edge("Bern", "Madrid", 1104)
    graph.new_edge("Madrid", "Genoa", 951)
    graph.new_edge("Madrid", "Paris", 805)
    graph.new_edge("Paris", "Brussels", 225)
    return graph


load_europe()
