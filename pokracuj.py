from logging import raiseExceptions


"""def červená():
    text=str(input("Zadejte text "))
    text.upper()
    délka=len(text)
    i=0
    while i<=délka-1:
        t=ord(text[i])
        početsudý=0
        početlichý=0
        if t%2==0:
            početsudý=početsudý+1
        else:
            početlichý=početlichý+1
        i=i+1
    if početsudý>početlichý:
        return True
    else: return False
print(červená()) """


mapa={} #tímto se tvoří prázdný cache v mapě
def odmocnina(num):
    if mapa.get(num) is not None:
        print("cache hit")
        return mapa.get(num)
    else:
        if num<0:
            raise Exception("Chybí mi komplexní čísla")
        else:
            odm=num**(1/2)
            mapa[num] = odm #v závorce klíč, za = hodnota
            return odm
num=int(input("Zadejte číslo "))
print(odmocnina(num))

print(mapa)

'''lass Seznam:
    def __init__(self,cislo:int,dalsi:"Seznam"):
        self.cislo=cislo    #tvoří si spojový seznam navázaný na okolní hodnotu
        self.dalsi=dalsi

class Spojovyseznam:
    def __init__(self) -> None:
        self._hlava:Seznam | None = None
    def is_empty(self):
        return self._hlava is None
    def prepend(self,nove_cislo:int): #vkládá číslo na začátek
        stary_prvni_prvek=self._hlava
        self._hlava=Seznam(nove_cislo,stary_prvni_prvek)
    def get(self,idx):
        acc=0 #acc = akumulátor (čítač)  
        if self.is_empty():
            raise Exception('prazdny seznam')   
        actual=self._hlava 
        while acc<idx:
            actual=actual.dalsi
            acc+=1  
        return actual'''
    
