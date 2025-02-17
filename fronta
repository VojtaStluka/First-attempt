from collections import deque
from dataclasses import dataclass
@dataclass
class Uloha:
    file:str
    user:str

class Printer():
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
