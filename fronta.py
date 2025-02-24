from collections import deque
from dataclasses import dataclass
@dataclass
class Uloha:
    file:str
    user:str

class Printer():    #fronta
    def __init__(self):
        self.f=deque()

    def enqueue (self,file,user):
        self.file=file
        self.user = user
        self.f.append(Uloha(file,user))
    
    def print_next(self):
        if len(self.f)<=0:
            print('Prázdno')
        else:
            print(self.f.popleft())

    def print_all(self):
        while len(self.f)>0:
            print (self.f.popleft())
        

printer = Printer()
printer.enqueue("tabulka.xls", "Karel")
printer.enqueue("referat.docx", "Lida")
printer.enqueue("dovolena.jpeg", "Rudolf")
printer.print_all()

class Browse_history(): #zásobník
    def __init__(self):
        self.historie = deque()
        self.budoucnost = deque()
        self.aktualni=""
    def open_page(self,url):
        self.historie.append(url)
        self.aktualni=url
    def go_back(self):
        self.budoucnost.append(self.aktualni)
        self.aktualni=self.historie.pop()
        print(self.aktualni)
    def go_forward(self):
        self.historie.append(self.aktualni)
        self.aktualni=self.budoucnost.pop()
        print(self.aktualni)
        
g=Browse_history()
g.open_page('Google')
g.open_page('Chrome')
g.open_page('Mozzila')
g.go_back()
g.go_back()
g.go_forward()
