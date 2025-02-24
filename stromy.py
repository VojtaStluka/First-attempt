from __future__ import annotations #řeší definování v definici (Uzel in Uzel)
from dataclasses import dataclass

@dataclass
class Uzel:
    operace: str
    levy: Uzel | None = None #quasi funkce or; když nic nedostane, nezlobí se
    pravy: Uzel | None = None

'''#operace 3+2
tri = Uzel('3')
dva = Uzel ('2')
plus = Uzel('+',tri,dva)'''


#operace (3+2)*4 - 8
tri = Uzel('3')
dva = Uzel ('2')
levy2= Uzel ('+',tri,dva)
ctyri = Uzel ('4')
levy=Uzel('*',levy2,ctyri)
osm = Uzel ('8')
minus=Uzel('-',levy,osm)

def tisk (n:Uzel):
    if (n.levy is None):
        print(n.operace)
    else: 
        tisk(n.levy)
        print(n.operace)
        tisk(n.pravy)

tisk(minus)
