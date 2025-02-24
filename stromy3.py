from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Optional, Any
from enum import Enum
from abc import ABC, abstractmethod

    

class Op(Enum):
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDE = "/"
    
    def __str__(self) -> str:
        return self.value


class Uzel(ABC):
    
    @abstractmethod
    def eval(self) -> float:
        pass


class ListUzel:

    def __init__(self, hodnota) -> None:
        self.hodnota = hodnota
    
    def __str__(self) -> str:
        return str(self.hodnota)
    
    def eval(self) -> float:
        return self.hodnota
        

class BinUzel:

    def __init__(self, operace, levy, pravy) -> None:
        self.operace = operace
        self.levy = levy
        self.pravy = pravy

    def __str__(self) -> str:
        return str(self.operace)
    
    def eval(self) -> float:
        l = self.levy.eval()
        p = self.pravy.eval()
        if self.operace == Op.PLUS:
            return l + p
        elif self.operace == Op.MINUS:
            return l - p
        elif self.operace == Op.TIMES:
            return l * p
        elif self.operace == Op.DIVIDE:
            return l / p
        else:
            raise ValueError(f"Neznama operace {self.operace}?")

def bfs(koren):
    fronta=deque()
    seznam=[]
    fronta.append(koren)
    while fronta:   #dokud fronta není prázdná
        celo=fronta.popleft()
        seznam.append(celo)
        if isinstance (celo,BinUzel):   #kontroluje, zda-li je celo binární uzel
            fronta.append(celo.levy)
            fronta.append(celo.pravy)
    return seznam
        

uzel10 = ListUzel(10)
uzel5 = ListUzel(5)
uzel3 = ListUzel(3)
uzel_plus = BinUzel(Op.PLUS, uzel10, uzel5)
uzel_krat=BinUzel(Op.TIMES,uzel3,uzel_plus)
lst = bfs(uzel_krat)
