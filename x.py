import os, binascii, base58
from hashlib import sha256
import random

def hex(x):
    return binascii.hexlify(x).decode()

# generating private key 
priv_key = bytes([random.randint(0, 255) for x in range(32)])

fullkey = b"\x80" + priv_key
sha256a = sha256(fullkey).digest()
sha256b = sha256(sha256a).digest()
WIF = base58.b58encode(fullkey+sha256b[:4])
print(WIF)

# print(hex(sha256b))
# sha256a = sha256(fullkey).digest()
# sha256b = sha256(sha256a).digest()
# WIF = base58.b58decode(fullkey+sha256b[:4])
# print(shex(fullkey))

# WIF = base58.b58encode(binascii.unhexlify(final_key))
# print (WIF)

#ecdsa y² = x³ + ax + b secp256k1 