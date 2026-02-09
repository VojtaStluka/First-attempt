from pydantic import BaseModel 
import datetime


class LogPristupu(BaseModel):
    rfid: str
    cas: datetime.datetime
    povoleno: bool

logy: list[LogPristupu] = []
class Turniket(BaseModel):
    platne_skipasy: list[str] = [] 
    log_pristupu: list[LogPristupu] = []

def vpustit(turniket: Turniket, rfid: str) -> bool:
    prosel = rfid in turniket.platne_skipasy
    turniket.log_pristupu.append(LogPristupu(rfid=rfid, cas=datetime.datetime.now(), povoleno=prosel))
    return prosel

def reset() -> None:
    global _platne_skipasy
    _platne_skipasy = []

def iniciace(skipasy: list[str]) -> None:
    global _platne_skipasy
    _platne_skipasy = skipasy

def pridej(zakoupeny_skipas_rfid: str) -> None:
    _platne_skipasy.append(zakoupeny_skipas_rfid)

'''demo'''

from turniket import *

if __name__ == "__main__":  
    turniket = Turniket()
    iniciace(["RFID123", "RFID456", "RFID789"])
    
    rfid_test = "RFID123"
    if vpustit(turniket, rfid_test):
        print(f"Uživatel s RFID {rfid_test} prošel turniketem.")
    else:
        print(f"Uživatel s RFID {rfid_test} neprošel turniketem.")
    
    pridej("RFID999")

