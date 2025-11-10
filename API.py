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


STUDENTI = [
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

# Globální proměnná s mapou studentů
_studenti: dict[str, Student] = {}

def inicializuj_studenty():
    """Inicializuje globální mapu studentů"""
    global _studenti
    for student in STUDENTI:
        _studenti[student.jmeno] = student

def pridej_studenta(student: Student) -> bool:
    """Přidá nového studenta. Vrací True pokud se podařilo přidat, False pokud už existuje"""
    if student.jmeno in _studenti:
        return False
    _studenti[student.jmeno] = student
    return True

def vypis_vsechny_studenty() -> list[Student]:
    """Vrátí seznam všech studentů"""
    return list(_studenti.values())

def najdi_studenty_podle_oboru(obor: Obor) -> list[Student]:
    """Vyhledá všechny studenty studující daný obor"""
    return [student for student in _studenti.values() if student.obor == obor]
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


STUDENTI = [
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

# Globální proměnná s mapou studentů
_studenti: dict[str, Student] = {}

def inicializuj_studenty():
    """Inicializuje globální mapu studentů"""
    global _studenti
    for student in STUDENTI:
        _studenti[student.jmeno] = student

def pridej_studenta(student: Student) -> bool:
    """Přidá nového studenta. Vrací True pokud se podařilo přidat, False pokud už existuje"""
    if student.jmeno in _studenti:
        return False
    _studenti[student.jmeno] = student
    return True

def vypis_vsechny_studenty() -> list[Student]:
    """Vrátí seznam všech studentů"""
    return list(_studenti.values())

def najdi_studenty_podle_oboru(obor: Obor) -> list[Student]:
    """Vyhledá všechny studenty studující daný obor"""
    return [student for student in _studenti.values() if student.obor == obor]

def najdi_studenty_podle_jmena(jmeno: str) -> list[Student]:
    """Najde všechny studenty se stejným jménem"""
    return [student for student in _studenti.values() if student.jmeno == jmeno]

def najdi_studenta_podle_rc(rodne_cislo: str) -> Student | None:
    """Vyhledá studenta podle rodného čísla"""
    for student in _studenti.values():
        if student.rodne_cislo == rodne_cislo:
            return student
    return None

# Inicializace při importu
inicializuj_studenty()
      

def najdi_studenty_podle_jmena(jmeno: str) -> list[Student]:
    """Najde všechny studenty se stejným jménem"""
    return [student for student in _studenti.values() if student.jmeno == jmeno]

def najdi_studenta_podle_rc(rodne_cislo: str) -> Student | None:
    """Vyhledá studenta podle rodného čísla"""
    for student in _studenti.values():
        if student.rodne_cislo == rodne_cislo:
            return student






#aplikace
from ./mapy_zas import *

def main():
    print("=== Systém správy studentů ===\n")
    
    # Vyhledání studenta
    print("1. Vyhledání studenta:")
    student = najdi_studenta("Jan Novák")
    if student:
        print(f"Nalezen: {student.jmeno}, RC: {student.rodne_cislo}, Obor: {student.obor.value}")
    else:
        print("Student nenalezen")
    
    print()
    
    # Vyhledání podle oboru
    print("2. Studenti oboru INFORMATIKA:")
    informatici = najdi_studenty_podle_oboru(Obor.INFORMATIKA)
    for student in informatici:
        print(f"- {student.jmeno}, RC: {student.rodne_cislo}")
    
    print()
    
    # Vyhledání podle jména (po přidání duplicitního jména)
    print("3. Přidání studenta se stejným jménem:")
    duplicitni = Student("Jan Novák", "9901019999", Obor.MATEMATIKA)
    if pridej_studenta(duplicitni):
        print(f"Student {duplicitni.jmeno} byl úspěšně přidán")
    else:
        print(f"Student {duplicitni.jmeno} již existuje (nelze přidat duplicitní jméno)")
    
    # Vyhledání podle rodného čísla
    print("\n4. Vyhledání podle rodného čísla:")
    student_rc = najdi_studenta_podle_rc("0152021345")
    if student_rc:
        print(f"Nalezen: {student_rc.jmeno}, RC: {student_rc.rodne_cislo}, Obor: {student_rc.obor.value}")
    else:
        print("Student s tímto RC nenalezen")
    
    print()
    
    # Výpis všech studentů
    print("5. Seznam všech studentů:")
    for student in vypis_vsechny_studenty():
        print(f"- {student.jmeno}, RC: {student.rodne_cislo}, Obor: {student.obor.value}")

if __name__ == "__main__":
    main()
      













_''''
