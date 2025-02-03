from __future__ import annotations #řeší definování v definici (Uzel in Uzel)
from dataclasses import dataclass
from abc import abstractmethod
from typing import Optional
from enum import Enum

class Uzel:
    operace: str
    levy: Uzel | List
    pravy: Uzel| List

    @abstractmethod
    def eval(self) -> float: #kontrakt
        ...

class Operace(Enum):
    PLUS = 0
    MINUS = 1
    KRAT = 2
    DELENO = 3


@dataclass
class UOperace(Uzel):
    operace: Operace
    levy: Uzel | List
    pravy: Uzel| List

    def eval(self) -> float:
        if self.operace == Operace.PLUS:
            return self.levy.eval() + self.pravy.eval()
        elif self.operace == Operace.MINUS:
            return self.levy.eval() - self.pravy.eval()
        elif self.operace == Operace.KRAT:
            return self.levy.eval() * self.pravy.eval()
        else:
            return self.levy.eval() / self.pravy.eval()

@dataclass
class List(Uzel):
    hodnota: int

    def eval(self) -> float:
        return self.hodnota

uzel10=List(10)
uzel8=List(8)
uzelplus=UOperace(Operace.KRAT,uzel10,uzel8)
print(uzelplus.eval())
