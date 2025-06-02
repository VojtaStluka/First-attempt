import hashlib
import rsa
#rsa
pub, priv = rsa.newkeys(512)

zprava="Zítra bude děsně pršet".encode()

zasifrovane=rsa.encrypt(zprava,pub)

print(zasifrovane)

desifrovane=rsa.decrypt(zasifrovane,priv)

print(desifrovane.decode())

#hashlib
zprava=b"Ahoj, jak se mas?"
hash=hashlib.md5(zprava)
'''soucet=0
vaha=1
for znak in zprava:
    soucet = soucet + znak*vaha
    vaha=256*vaha
    soucet=soucet%1000007'''
print(hash.hexdigest())
