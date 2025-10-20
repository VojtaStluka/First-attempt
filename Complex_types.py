def add_numbers(a: int | float, b: int | float) -> int | float:
    return a + b

def format_name(first: str, last: str, upper: bool) -> str:
    name = f"{first} {last}"
    if upper:
        return name.upper()
    return name

def suda_cisla(seznam: list[int]) -> list[int]:
    vysledek: list[int] = []
    for cislo in seznam:
        if cislo%2 == 0:
            vysledek.append(cislo)
    return vysledek
    
print(suda_cisla([1,5,4,6,3,2]))

seznam=[1,5,4,6,3,2]
print([cislo for cislo in seznam if cislo%2==0])

studenti_tuple = [
    ("Jan Novák", 20, "informatika"),
    ("Marie Svobodová", 22, "matematika"),
    ("Petr Dvořák", 19, "fyzika"),
    ("Lucie Němcová", 21, "ekonomie"),
    ("Tomáš Černý", 23, "informatika"),
    ("Karolína Procházková", 20, "matematika"),
    ("Jakub Kučera", 18, "informatika"),
    ("Tereza Veselá", 22, "fyzika"),
    ("Martin Horák", 21, "ekonomie"),
    ("Veronika Marková", 19, "informatika"),
    ("Filip Pospíšil", 24, "matematika"),
    ("Anna Králová", 20, "fyzika"),
    ("David Beneš", 22, "ekonomie"),
    ("Kristýna Růžičková", 19, "informatika"),
    ("Ondřej Fiala", 21, "matematika"),
    ("Barbora Malinová", 23, "fyzika"),
    ("Michal Sedláček", 20, "ekonomie"),
    ("Nikola Doležalová", 18, "informatika"),
    ("Adam Nguyen", 22, "fyzika"),
    ("Eliška Krejčí", 21, "matematika")]

def vyber_studenty(studenti: list[tuple[str,int,str]], min_vek: int) -> list[tuple[str,int,str]]:
    vybrani = [student for student in studenti if student[1] >= min_vek]
    return vybrani
print(vyber_studenty(studenti_tuple, 21))








