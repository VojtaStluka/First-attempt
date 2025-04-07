from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 
class BinaryHeap:

    def __init__(self):
        self.heap: list[Element] = []
        
    def push(self,element:Element):
        self.heap.append(element)
        idx=(len(self.heap))-1
        while idx>0:
            idx_rodic = (idx-1) // 2
            rodic = self.heap[idx_rodic] 
            dite = element           
            if rodic.priority > dite.priority:
                self.heap[idx] = rodic
                self.heap[idx_rodic] = dite
            else: 
                break
         

    def pop(self):
        min_element=self.heap[0]
        last_element=self.heap.pop()    #najdeme poslední prvek
        if not self.heap: #Pokud jsme odstranili poslední prvek, vrátíme rovnou
            return min_element
        else:
            self.heap[0]=last_element   #prohodíme do kořene
            idx=0

            while True:
                smallest=idx
                left_child = 2 * idx + 1
                right_child = 2 * idx + 2
                if left_child <= len(self.heap)-1 and self.heap[left_child].priority < self.heap[smallest].priority:    #kontrola min_heap a zároveň kontrola, jestli existuje (v poslední vrstvě být nutně nemusí)
                        smallest = left_child
                if  right_child <= len(self.heap)-1 and self.heap[right_child].priority < self.heap[smallest].priority:
                        smallest = right_child
                if smallest != idx:
                    self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]   #prohození ve vrstvách
                    idx = smallest
                else: 
                    break
            return min_element


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        min_idx = 0
        return self.heap[min_idx]



"""
from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, element):
        self.heap.append(element)
        current_index = len(self.heap) - 1
        
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.heap[parent_index].priority > self.heap[current_index].priority:
                self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
                current_index = parent_index
            else:
                break

    def pop(self):
        if not self.heap:
            return None
        
        min_element = self.heap[0]
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            index = 0
            while True:
                smallest = index
                left = 2 * index + 1
                right = 2 * index + 2
                
                if left < len(self.heap) and self.heap[left].priority < self.heap[smallest].priority:
                    smallest = left
                
                if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
                    smallest = right
                
                if smallest == index:
                    break
                
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
        
        return min_element


    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        # vrati nejmensi element ve fronte (element na cele fronty)
        # protoze mame naivni implementaci, musime projit cely seznam
        min_idx = 0
        for idx in range(1,len(self.heap)):
            if self.heap[idx].priority < self.heap[min_idx].priority:
                min_idx = idx
        return self.heap[min_idx]
        """
