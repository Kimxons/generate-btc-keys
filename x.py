import os, binascii, base58, ecdsa, hashlib
from hashlib import sha256
import random

def make_qrcode(public_addr):
  import qrcode
  img = qrcode.make(public_addr)
  img.save("coin.png")

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

def get_key_with_seed(seed=1337):
  # generating private key
  random.seed(seed) 
  priv_key = bytes([random.randint(0, 255) for x in range(32)])

  #WIF from private key
def priv_key_to_public(priv_key):
  WIF = b58wchecksum(b"\x80" + priv_key)
  # print(WIF)

  #public key
  sk = ecdsa.SigningKey.from_string(priv_key, curve=ecdsa.SECP256k1)
  vk = sk.get_verifying_key()
  public_key = b"\x04" + vk.to_string()
  hash160 = ripemd160(sha256(public_key).digest()).digest()
  public_addr = b58wchecksum(b"\x00" + hash160)
  return priv_key, WIF, public_key, hash160, public_addr    