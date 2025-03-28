
from enum import Enum
from dataclasses import dataclass
from random import randint, choice, sample, seed

class TypPacienta(Enum):
    HYPOCHONDR = 0
    NORMAL = 1
    RAMBO = 2

class ZkusenostLekare(Enum):
    GREENHORN = 0
    NORMAL = 1
    EXPERT = 2

@dataclass
class Pacient:
    rodne_cislo: str
    jmeno_prijmeni: str
    vek: int
    typ: TypPacienta
    pohlavi_zena: bool


class Specializace(Enum):
    NEFROLOGIE = 0
    NEUROLOGIE = 1
    KARDIOLOGIE = 2
    CHIRURGIE = 3
    ORL = 4


@dataclass
class Lekar:
    jmeno_prijmeni: str
    specializace: Specializace
    zkusenosti: ZkusenostLekare

class Ordinace:
    def __init__(self,specializace:Specializace,hlavni_lekar: Lekar,pomocny_lekar: Lekar,pacienti: list[Pacient],max_obsazeni: int):
        self.specializace=specializace
        self.hlavni_lekar=hlavni_lekar
        self.pomocny_lekar=pomocny_lekar
        self.pacienti=pacienti
        self.max_obsazeni=max_obsazeni

    def prida_pacienta(self,pacient):       
        x=len(self.pacienti)
        if (x>self.max_obsazeni):
            raise Exception("Příliš mnoho!")
        self.pacienti.append(pacient)




@dataclass
class Nemocnice:
    ordinace: list[Ordinace]


def generuj_nemocnici(tisk: bool, pocet_ordinaci) -> Nemocnice:
    seed(42)

    # Helper functions
    def generate_pacient(rodne_cislo, jmeno_prijmeni):
        vek = randint(1, 100)
        typ = choice(list(TypPacienta))
        pohlavi_zena = choice([True, False])
        return Pacient(rodne_cislo, jmeno_prijmeni, vek, typ, pohlavi_zena)

    def generate_lekar(jmeno_prijmeni, specializace,zkusenosti):
        return Lekar(jmeno_prijmeni, specializace,zkusenosti)

    # Generate shared patients
    shared_pacienti = [
        generate_pacient(f"{100000+idx}{idx}", f"Shared Pacient {idx}") for idx in range(5)
    ]

    # Generate ordinace and nemocnice
    ordinace_list = []
    specializace_list = list(Specializace)
    zkusenosti_list = list(ZkusenostLekare)

    for i in range(pocet_ordinaci):
        specializace = specializace_list[i % len(specializace_list)]
        zkusenosti = zkusenosti_list[i % len(zkusenosti_list)]
        hlavni_lekar = generate_lekar(f"Hlavni Lekar {i}", specializace, zkusenosti)
        pomocny_lekar = generate_lekar(f"Pomocny Lekar {i}", choice(list(Specializace)),choice(list(ZkusenostLekare))) if i % 2 == 0 else None

        pacienti = shared_pacienti + [
            generate_pacient(f"{100000+i}{j}", f"Pacient {i}-{j}") for j in range(7)
        ]
        pacienti = sample(pacienti, len(pacienti))  # Shuffle patients

        ordinace_list.append(
            Ordinace(
                specializace=specializace,
                hlavni_lekar=hlavni_lekar,
                pomocny_lekar=pomocny_lekar,
                pacienti=pacienti,max_obsazeni=randint(20,30)
            )
        )

    nemocnice = Nemocnice(ordinace=ordinace_list)

    # Output for verification
    if tisk:
        for ord in nemocnice.ordinace:
            print(f"Ordinace: {ord.specializace}")
            print(f"  Hlavni lekar: {ord.hlavni_lekar}")
            if ord.pomocny_lekar:
                print(f"  Pomocny lekar: {ord.pomocny_lekar}")
            print("  Pacienti:")
            for pacient in ord.pacienti:
                print(f"    {pacient}")
            print()
    return nemocnice

nemocnice = generuj_nemocnici(False, 4)

"""
*Pacient*
- rodné číslo
- jméno + příjmení
- věk
- typ: hypochondr, normal, superman
*Lékař*
- jméno + příjmení
- zkušenost: zaučuji se, normal, expert
- obor: kardio, nefro, neuro, orl, interna, radio, gynekologie
*Ordinace*
- název: jakékoliv pojmenování
- kapacita
- seznam pacientů
- hlavní lékař
- pomocný lékař
*Nemocnice*
- seznam ordinací


*Dynamika*
- ordinaci předěláme na normální třídu
- na ordinaci bychom chtěli následující metody:
1. přidej pacienta: signalizuje výjimkou, pokud je ordinace přes kapacitu
2. vrať všechny hypochondry
3. má ordinace volnou kapacitu?: vrací boolean true/false
- nemocnici předěláme na normální třídu
- na nemocnici bychom chtěli následující metody:
1. vrať seznam všech specializací, které nemocnice nabízí
   (procházením ordinací a sběrem jejich specializací)
2. vrať seznam ordinací, které mají ještě volnou kapacitu
3. vrať seznam všech pacientů nemocnice
4. vrať seznam všech expertů v nemocnici
5. umí specializaci?: vrací true/false podle toho zda hlavní nebo pomocný
   lékař některé z ordinací má danou specializaci
"""