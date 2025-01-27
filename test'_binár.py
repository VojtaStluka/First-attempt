def binarni(seznam,cil):

    levy=0
    pravy = len(seznam)-1
   
    while levy < pravy:
        prostredni=(pravy + levy)//2
        if cil == seznam[prostredni]:
            return prostredni
        elif cil>seznam[prostredni]:
            print(f"levy nastavuji do {prostredni})")
            print(f"pravy je {pravy}")
            levy = prostredni + 1
        elif cil<seznam[prostredni]:
            print(f"pravy nastavuji do {prostredni})")
            print(f"levy je {levy}")
            pravy = prostredni - 1
        else: 
            print("levy" + str(levy))
            print("pravy" + str(pravy))
            print("prostredni" + str(prostredni))
            raise Exception("?")

    return None
            

print(binarni([-8,-7,-3,0,1,1,3,7,8,10],1))


'''from dataclasses import dataclass

@dataclass 
class Karta:
    id: str

class Zamestnanec:
    
    def __init__(self, jmeno, prijmeni,id_karty:Karta):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._karty = {}
        self.id_karty=id_karty

    def pridej(self,karta):
        if self._karty.get(self.id_karty) is not None:
            raise Exception ("už je tu.")
        self._karty[self.id_karty]=karta

    def kontrola(self,id_karty):
        if self._karty.get(id_karty) is True:
            True
        else: False

'''