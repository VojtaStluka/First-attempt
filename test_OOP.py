from dataclasses import dataclass

@dataclass
class Mistnost:
    jmeno:str
    rozloha:int

@dataclass
class Polozka:
    kod:str
    nazev:str
    cena:int
    umisteni:str
    x:int
 

class Sklad:
    def __init__(self,mistnost:list[Mistnost]):        
        self.mistnost=mistnost
        self.polozky={}
    
    def zaloz(self,kod:str,nazev:str,cena:int,umisteni:str): 
        x=0       
        if kod in self.polozky:
            raise Exception("Už je tu!")
        if umisteni != Mistnost.jmeno:
            raise Exception ("Neexistuje")
        self.polozky[kod]=Polozka(kod,nazev,cena,umisteni,x)

    def naskladni(self,kod,a):
        self.polozky.get(kod).x+=a

    def vyskladni(self,kod,b):
        if b>self.polozky.get(kod).x:
                raise Exception("Neztratit")
        self.polozky.get(kod).x-=b
                          

    def najdi(self,kod):
        if kod in self.polozky:
            print(self.polozky.get[kod])
        else: print("None")

    



###############################################################################################
## pojdme vse otestovat:

mistnostA1 = Mistnost("A1", 43)
mistnostA2 = Mistnost("A2", 200)
mistnostA3 = Mistnost("A3", 120)

sklad = Sklad([mistnostA1, mistnostA2, mistnostA3])
# zalozime polozky:
sklad.zaloz("AB00010034", "mleko", 32.90, "A1")
sklad.zaloz("AB999888237", "maslo", 92.00, "A1")
sklad.zaloz("AB00010037", "chleba", 63.50, "A3")

# test
try:
    sklad.zaloz("AB00010034", "traktor", 3_450_230, "A2")
    # spatne, takovy carovy code jiz by pouzity, mela vyletet vyjimka
    assert False, "carovy kod AB00010034 je jiz pouzity, proc se podarilo zalozit?"
except:
    # OK, ocekavane
    ...

# test
try:
    sklad.zaloz("AB00010777", "obusek", 20.50, "AA2")
    # spatne, takova mistnost neexistuje, mela vyletet vyjimka
    assert False, "AA2 mistnost neexistuje, proc se podarilo zalozit?"
except:
    # OK, ocekavane
    ...

# naskladnime polozky:
sklad.naskladni("AB00010034", 100)      # mleko
sklad.naskladni("AB00010034", 11)
sklad.naskladni("AB999888237", 200)     # maslo

# vyskladnime
sklad.vyskladni("AB00010034", 30)

# test:
try:
    sklad.vyskladni("AB00010034", 300)
    assert False, "nemohu vyskladnovat nad-pocet polozek"
except:
    # OK, ocekavame
    ...


assert sklad.najdi("BB023802347") is None
mleko = sklad.najdi("AB00010034")
assert mleko is not None
assert mleko.pocet == 81
assert mleko.mistnost == mistnostA1
assert mleko.kod == "AB00010034"
assert mleko.nazev == "mleko"
assert mleko.cena == 32.90

assert sklad.nejvetsi_mistnost() == mistnostA2

assert sklad.kde_je("NEEX-CAROVY-KOD") is None
assert sklad.kde_je("AB00010037") is mistnostA3

print("vyborne, nejspis vse funguje jak ma")