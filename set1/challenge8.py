import json
import binascii
import pprint
from collections import Counter
from Crypto.Cipher import AES
from base64 import *
pp = pprint.PrettyPrinter(indent=4)
def read_file():
    return (open("8.txt", "rb").read())

cipher_text = read_file().splitlines()

for line in cipher_text:
    chunk_size = 16
    line = binascii.unhexlify(line)
    chunks = []
    so_far = 0
    while True:
        chunks.append(line[so_far:so_far+chunk_size])
        so_far += chunk_size
        if so_far >= len(line):
            break
    print json.dumps(Counter([binascii.hexlify(chunk) for chunk in chunks]), indent=4)
            
