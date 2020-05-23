import os, binascii, base58, ecdsa, hashlib
from hashlib import sha256
import random

def hex(x):
    return binascii.hexlify(x).decode()

def dbl256(x):
  return sha256(sha256(x).digest()).digest()

def checksum(x):
  return dbl256(x)[:4]

def b58wchecksum(x):
  return base58.b58encode(x+checksum(x))

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d   

# generating private key
random.seed(1337) 
priv_key = bytes([random.randint(0, 255) for x in range(32)])

#private key to WIF
# fullkey = b"\x80" + priv_key
# sha256a = sha256(fullkey).digest()
# sha256b = sha256(sha256a).digest()
# WIF = base58.b58encode(fullkey+sha256b[:4])
fullkey = b"\x08" + priv_key
WIF = b58wchecksum(fullkey)
print(WIF)

#public key
sk = ecdsa.SigningKey.from_string(priv_key, curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()
public_key = b"\x04" + vk.to_string()
hash160 = ripemd160(sha256(public_key).digest()).digest()
public_addr_a = b"\x80" + hash160
public_addr_b = b58wchecksum(public_addr_a)
print(public_addr_b)


# print(hex(sha256b))
# sha256a = sha256(fullkey).digest()
# sha256b = sha256(sha256a).digest()
# WIF = base58.b58decode(fullkey+sha256b[:4])
# print(shex(fullkey))

# WIF = base58.b58encode(binascii.unhexlify(final_key))
# print (WIF)

#ecdsa y² = x³ + ax + b secp256k1 