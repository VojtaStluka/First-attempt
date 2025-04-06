from dataclasses import dataclass
from typing import List, Tuple, Dict

@dataclass
class City:
    name:str
    neighbors: List[Tuple[str, int]]  # list of (neighbor_name, distance)

class Graph:
    def __init__(self):
        self.cities: Dict[str, City] = {}

    def add_edge(self, from_city: str, to_city: str, distance: int):
        if from_city not in self.cities:
            self.cities[from_city] = City(from_city, [])
        if to_city not in self.cities:
            self.cities[to_city] = City(to_city, [])

        self.cities[from_city].neighbors.append((to_city, distance))
        self.cities[to_city].neighbors.append((from_city, distance))  # undirected

    def get_neighbors(self, city_name: str) -> List[Tuple[str, int]]:
        return self.cities[city_name].neighbors
    
    def total_cities(self):
        return len(self.cities)
    
    def path_exists(self, from_city: str, to_city: str) -> bool:
        for neighbor, _ in self.get_neighbors(from_city):
            if neighbor == to_city:
                return True
        return False

class Path:
    def __init__(self, visited: List[str], total_distance: int):
        self.visited = visited
        self.total_distance = total_distance

    def extend(self, next_city: str, distance: int) -> 'Path':
        return Path(self.visited + [next_city], self.total_distance + distance)
    

