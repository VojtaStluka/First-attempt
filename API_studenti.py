#pro uživatele:
from API_studenti import *

studenti = [
    Student("Jan Novák", "9901011234", Obor.INFORMATIKA),
    Student("Marie Svobodová", "0152021345", Obor.MATEMATIKA),
    Student("Petr Dvořák", "0203031456", Obor.FYZIKA),
    Student("Lucie Němcová", "0054041567", Obor.EKONOMIE),
    Student("Tomáš Černý", "9805051678", Obor.INFORMATIKA),
    Student("Karolína Procházková", "0256061789", Obor.MATEMATIKA),
    Student("Jakub Kučera", "0407071890", Obor.INFORMATIKA),
    Student("Tereza Veselá", "0158081901", Obor.FYZIKA),
    Student("Martin Horák", "9909092012", Obor.EKONOMIE),
    Student("Veronika Marková", "0160102123", Obor.INFORMATIKA),
    Student("Filip Pospíšil", "9711112234", Obor.MATEMATIKA),
    Student("Anna Králová", "0262122345", Obor.FYZIKA),
    Student("David Beneš", "9913132456", Obor.EKONOMIE),
    Student("Kristýna Růžičková", "0164142567", Obor.INFORMATIKA),
    Student("Ondřej Fiala", "9915152678", Obor.MATEMATIKA),
    Student("Barbora Malinová", "0066162789", Obor.FYZIKA),
    Student("Michal Sedláček", "9917172890", Obor.EKONOMIE),
    Student("Nikola Doležalová", "0268182901", Obor.INFORMATIKA),
    Student("Adam Nguyen", "9919193012", Obor.FYZIKA),
    Student("Eliška Krejčí", "0070203123", Obor.MATEMATIKA),
]

#nahraje studenty do mapy při importu
inicializuj_studenty(studenti)

#přidá nového studenta
pridej_studenta(Student("Petr Dvořák", "0012203544", Obor.MATEMATIKA))

#vypíše studenty
seznam = vypis_vsechny_studenty()
print("Seznam všech studentů:"+str(seznam))

#vyhledá studenty podle oboru
r = najdi_studenty_podle_oboru(Obor.INFORMATIKA)
print (r)

#najde stejná jména, jsou-li nějaká
s = najdi_stejna_jmena()
print(s)

#efektivně hledá podle RČ
c= najdi_studenta_podle_rc("9901011234")
print(c)


'''Dát do jiného souboru'''

#vnitřek aplikace:
from enum import Enum
from dataclasses import dataclass

class Obor(Enum):
    INFORMATIKA = "informatika"
    MATEMATIKA = "matematika"
    FYZIKA = "fyzika"
    EKONOMIE = "ekonomie"

@dataclass
class Student:
    jmeno: str
    rodne_cislo: str
    obor: Obor

_studenti: dict[str, Student] = {}

def inicializuj_studenty(seznam_studentů: list[Student]) -> None:
    global _studenti
    for s in seznam_studentů:
        # RČ je klíč do mapy studentů
        _studenti[s.rodne_cislo] = s

def pridej_studenta(student: Student) -> bool:
    #Přidá nového studenta do mapy podle RČ, již existující RČ nahlásí jako chybu.
    if student.rodne_cislo in _studenti:
        return False
    _studenti[student.rodne_cislo] = student
    return True

def vypis_vsechny_studenty() -> list[Student]:
    #Vrátí seznam všech studentů.
    return list(_studenti.values())

def najdi_studenty_podle_oboru(obor: Obor) -> list[Student]:
    #Vyhledá všechny studenty studující daný obor.
    return [student for student in _studenti.values() if student.obor == obor]

def najdi_studenta_podle_rc(rodne_cislo: str) -> Student | None:
    #Efektivně vyhledá studenta podle rodného čísla.
    return _studenti.get(rodne_cislo)

def najdi_stejna_jmena() -> dict[str, list[Student]]:  
    # Vytvoří slovník pro seskupení studentů podle jména
    seznam_jmen: dict[str, list[Student]] = {}

    # Projde všechny studenty a seskupí je podle jména
    for student in _studenti.values():
        # Pokud jméno ještě není ve slovníku, vytvoříme pro ono jméno prázdný seznam
        if student.jmeno not in seznam_jmen:
            seznam_jmen[student.jmeno] = []
        # Přidáme studenta do normálního seznamu pro jeho jméno
        seznam_jmen[student.jmeno].append(student)
    
    # Vytvoří slovník jen pro duplicitní jména
    duplicitni: dict[str, list[Student]] = {}
    # Projde všechna jména a zachová jen ta, která má více studentů
    for jmeno, studenti in seznam_jmen.items():
        #Pokud má seznam jmen u daného jména více než jednoho studenta
        if len(studenti) > 1:
            duplicitni[jmeno] = studenti
    
    return duplicitni

