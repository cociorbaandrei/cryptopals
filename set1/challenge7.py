from Crypto.Cipher import AES
from base64 import *

def read_file():
    return b64decode(open("7.txt", "rb").read())

cipher_text = read_file()
key = "YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(cipher_text)
print decrypted
