"""#Bubble sort
seznam=[]   #vytváří si seznam čísel
novy_seznam=[]
def bubble(seznam):     #bude řadit vzestupně
    if seznam is None:  #řeší prázný seznam
        pass
    else:
        i=0        
        while i<=len(seznam):
            prvek=prvek[i]  #prvek na prvním místě
            druhy=prvek[i+1]    #na místě o 1 větším
            for prvek in seznam:
                if prvek > druhy:
                    novy_seznam.append(druhy)   #přidává první ten menší
                    novy_seznam.append(prvek)
                else:
                    novy_seznam.append(prvek)   #nechává první ten menší
                    novy_seznam.append(druhy)
            i=i+1
    return novy_seznam
seznam=int(input("Zadejte čísla "))
print(bubble(seznam))
        """
class Zak:
	def __init__(self, jmeno, prijmeni, rodne_cislo):
		self.jmeno = jmeno
		self.prijmeni = prijmeni
		self.rodne_cislo = rodne_cislo
		
	def __eq__(self, other):
		return self.jmeno == other.jmeno and self.prijmeni == other.prijmeni
class Skola:
	
    def __init__(self):
        self._zaci = {}
    def pridej(self,rodne_cislo,zak):
        self._zaci[rodne_cislo]=zak
    def najdi(self, rodne_cislo):
        for z in self._zaci:
            if z.rodne_cislo == rodne_cislo:
                return z
        return None
# zkusebni kod
skola = Skola()	
z = Zak("Karel", "Svoboda", "1122335566")
skola.pridej(z)
print(skola.najdi("1122335566").jmeno)