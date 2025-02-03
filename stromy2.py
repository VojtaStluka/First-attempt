from __future__ import annotations #řeší definování v definici (Uzel in Uzel)
from dataclasses import dataclass
from typing import Optional

class Uzel:
    operace: str
    levy: Uzel | List
    pravy: Uzel| List
    def tisk(self):
        ...

@dataclass
class UOperace(Uzel):
    operace: str
    levy: Uzel | List
    pravy: Uzel| List
    def tisk(self):
        print("Jsem vnitřní uzel")
        self.levy.tisk()
        print(self.operace)
        self.pravy.tisk()

@dataclass
class List(Uzel):
    hodnota: int
    def tisk(self):
        print(self.hodnota)


'''#operace (3+2)*4 - 8
tri = Uzel('3')
dva = Uzel ('2')
levy2= Uzel ('+',tri,dva)
ctyri = Uzel ('4')
levy=Uzel('*',levy2,ctyri)
osm = Uzel ('8')
minus=Uzel('-',levy,osm)'''


uzel10=List(10)
uzel8=List(8)
uzelplus=UOperace('+',uzel10,uzel8)
uzelplus.tisk()