def encrypt_letter(letter,shift):
    if letter.isalpha(): #je-li písmenem
        base = ord('A') if letter.isupper() else ord("a")
        return chr((ord(letter) - base + shift) % 26 + base)
    else:
        raise ValueError("Nevhodný formát: {}".format(letter))

def encrypt_message(message,shift):
    vysledek=""
    for letter in message:
        if not letter.isalpha(): #řeší problém mezer a jiných než písmenných znaků
            vysledek += letter
        else:
            vysledek+=encrypt_letter(letter,shift) #vysledek=vysledek+encrypt_letter()
    return vysledek

print(encrypt_letter("A",3))
print(encrypt_letter("Z",6))
encoded=(encrypt_message("To claim the hidden 1 million CZK, start by locating the old oak tree near the abandoned railway station. From there, walk exactly 147 steps north until you reach a small stone marked with a red \"X\". Beneath the stone, you will find a metal box containing further instructions. Follow them carefully — only those who pay close attention to every detail will reach the final reward.",3))


def decrypt_letter(letter,shift):
    if letter.isalpha(): #je-li písmenem
        base = ord('A') if letter.isupper() else ord("a")
        return chr((ord(letter) - base - shift) % 26 + base)
    else:
        raise ValueError("Nevhodný formát: {}".format(letter))

def decrypt_message(message,shift):
    vysledek=""
    for letter in message:
        if not letter.isalpha(): #řeší problém mezer a jiných než písmenných znaků
            vysledek += letter
        else:
            vysledek+=decrypt_letter(letter,shift) #vysledek=vysledek+encrypt_letter()
    return vysledek
    
print(decrypt_message(encoded,3))

message="Kyv grky kf kyv yzuuve 125 fletvj fw xfcu svxzej rk kyv efikyvie xrkv fw kyv fcu tvdvkvip. Giftvvu vrjknriu rcfex kyv tirtbvu jkfev nrcc wfi rggifozdrkvcp 150 dvkvij, lekzc pfl uzjtfmvi r xrkv tfmvivu ze zmp. Svyzeu zk, slizvu yrcw r dvkvi uvvg svevrky kyv kyziu xirmvjkfev fe kyv cvwk, czvj r jvrcvu vemvcfgv. Zejzuv, pfl nzcc wzeu kyv wzerc tclv evvuvu kf lecftb pfli gizqv. Jkrp jyrig — efk vmvipkyzex zj rj zk jvvdj."
for number in range(26):
    print(decrypt_message(message,number))
    print(number)



def encrypt_with_key(text,key):
    vysledek=""
    indexy=[ord(k.lower())for k in key] #list comprehensions [funkce for prvek in seznam]
    key_len=len(key)
    for i,char in enumerate(text):  #vyhodí posloupnost indexu a položky na něm
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = indexy[i % key_len]
            vysledek += chr((ord(char) - base + shift) % 26 + base)
        else:
            vysledek += char
    return vysledek

print(encrypt_with_key("ahoj jak se mas","prezident"))

klic=b"arcibiskupskegymnazium"  #b z toho udělá sekvenmci čísel
soubor=open("test.pdf","rb")
obsah = soubor.read()

idx=0

delka=len(klic)
sifrovany_obsah=bytearray()
for b in obsah:
    sb = (b+klic[idx%delka])%256
    sifrovany_obsah.append(sb)
    idx+=1
sifrovany_soubor = open("test-sifrovany.bin","wb")
sifrovany_soubor.write(sifrovany_obsah)
soubor.close()
sifrovany_soubor.close()



k_desifrovani=open("test-sifrovany.bin","rb")
des_obsah=k_desifrovani.read()

desifrovany_obsah=bytearray()
idx=0
for b in des_obsah:
    sb = (b-klic[idx%delka])%256
    desifrovany_obsah.append(sb)
    idx+=1
desifrovany_soubor = open("desifrovany.pdf","wb")
desifrovany_soubor.write(desifrovany_obsah)
k_desifrovani.close()
desifrovany_soubor.close()
