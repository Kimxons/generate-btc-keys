import os, binascii
import hashlib, base58, ecdsa
from hashlib import sha256

# priv_key = os.urandom(32)

# fullkey = '80' + binascii.hexlify(priv_key).decode()
fullkey = '80' + binascii.hexlify(os.urandom(32)).decode()

sha256a = hashlib.sha256(binascii.unhexlify(fullkey)).hexdigest()
sha256a = sha256(binascii.unhexlify(fullkey)).hexdigest()
sha256b = sha256(binascii.unhexlify(sha256a)).hexdigest()
WIF = base58.b58decode(binascii.unhexlify(fullkey+sha256b[:4]))
print(fullkey)