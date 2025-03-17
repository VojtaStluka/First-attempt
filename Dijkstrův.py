class Mesto:
    def __init__(self,nazev:str):
        self.nazev=nazev
        self.soused: list[str]= []

class Graph:
    def __init__(self) -> None:
        self._mesta: dict[str,Mesto] = {}
    
    def new_edge(self, from_city: str, to_city: str, distance: int) -> None:
        self.mesto_z=self.zaloz(from_city)
        self.mesto_do=self.zaloz(to_city)
        self.mesto_z.soused.append([self.mesto_do,distance])
        self.mesto_do.soused.append([self.mesto_z,distance])
    
    def zaloz(self,nazev):
        mesto=self._mesta.get(nazev)
        if mesto is None:
            mesto=Mesto(nazev)
            self._mesta[nazev]=mesto
        return mesto

        
    def find_shortest_path(self, from_city: str, to_city: str) -> int:
        fronta=list[tuple[Mesto,Mesto]]=[]
        m = self._mesta[from_city]
        for mesto in self._mesta:
            fronta.append([mesto,self.soused])
            visited = set([mesto])

@dataclass
class Element:
    value:object
    priority:int

class PriorityQueue:
    def __init__(self):
        self.seznam=[]

    def push(self,*element:int):
        self.seznam.append(element)
        idx=len(self.seznam)-1
        dite=element
        if idx > 1:
            while True:
                if self.seznam[idx] < self.seznam[((idx-1)//2)]:
                    element [idx-1//2] = element [idx]
        print (self.seznam)

        
    def pop():
        ...

a=PriorityQueue()
a.push(4,6,3,1,5)
        
def init_distances() -> Graph:
        graph = Graph()
        graph.new_edge("Lisbon", "Madrid", 339)
        graph.new_edge("Naples", "Rome", 134)
        graph.new_edge("Hamburg", "Copenhagen", 180)
        graph.new_edge("Hamburg", "Berlin", 182)
        graph.new_edge("Berlin", "Warsaw", 345)
        graph.new_edge("Amsterdam", "Hamburg", 338)
        graph.new_edge("Amsterdam", "Brussels", 164)
        graph.new_edge("Berlin", "Prague", 219)
        graph.new_edge("Prague", "Warsaw", 479)
        graph.new_edge("Prague", "Vienna", 185)
        graph.new_edge("Munich", "Prague", 174)
        graph.new_edge("Vienna", "Warsaw", 464)
        graph.new_edge("Vienna", "Budapest", 214)
        graph.new_edge("Warsaw", "Budapest", 394)
        graph.new_edge("Budapest", "Belgrade", 319)
        graph.new_edge("Vienna", "Belgrade", 490)
        graph.new_edge("Budapest", "Trieste", 384)
        graph.new_edge("Trieste", "Vienna", 317)
        graph.new_edge("Trieste", "Belgrade", 403)
        graph.new_edge("Munich", "Vienna", 280)
        graph.new_edge("Munich", "Rome", 582)
        graph.new_edge("Genoa", "Trieste", 361)
        graph.new_edge("Genoa", "Rome", 328)
        graph.new_edge("Trieste", "Rome", 442)
        graph.new_edge("Paris", "Genoa", 629)
        graph.new_edge("Genoa", "Bern", 304)
        graph.new_edge("Genoa", "Brussels", 740)
        graph.new_edge("Bern", "Brussels", 497)
        graph.new_edge("Amsterdam", "Bern", 558)
        graph.new_edge("Amsterdam", "Munich", 526)
        graph.new_edge("Bern", "Munich", 311)
        graph.new_edge("Bern", "Trieste", 489)
        graph.new_edge("Bern", "Madrid", 1104)
        graph.new_edge("Madrid", "Genoa", 951)
        graph.new_edge("Madrid", "Paris", 805)
        graph.new_edge("Paris", "Brussels", 225)
        return graph


def test_prague_berlin():
        graph = init_distances()
        prg_bln_distance = graph.find_shortest_path("Prague", "Berlin")
        assert prg_bln_distance == 219


def test_belgrade_berlin():
        graph = init_distances()
        blg_bln_distance = graph.find_shortest_path("Belgrade", "Berlin")
        assert blg_bln_distance == 894


def test_prague_budapest():
        graph = init_distances()
        prg_bdp_distance = graph.find_shortest_path("Prague", "Budapest")
        assert prg_bdp_distance == 399

def test_madrid_naples():
        graph = init_distances()
        mdr_npl_distance = graph.find_shortest_path("Madrid", "Naples")
        assert mdr_npl_distance == 1413

def test_trieste_amsterdam():
    graph = init_distances()
    trs_ams_distance = graph.find_shortest_path("Trieste", "Amsterdam")
    assert trs_ams_distance == 1047
