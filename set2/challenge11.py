#!/bin/python2
from challenge10 import aes_cbc_encrypt
from challenge10 import encrypt_block
from random import randrange
import os
import binascii
from collections import Counter
import pprint


pp = pprint.PrettyPrinter(indent=4)

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def chunks16(data, encode=False):
    data = zip(*[ret[i::16] for i in range(16)])
    if not encode:
        return list(map(lambda l : "".join([chr(i) for i in l]), data))
    return list(map(lambda l : "".join([chr(i) for i in l]).encode("hex"), data))

def encryption_oracle(input):
    random_key = os.urandom(16)
    modified_input = os.urandom(randrange(5,11)) + input + os.urandom(randrange(5,11))
    encrypted = bytearray()
    if randrange(0,2) == 1:
        # do cbc
        iv = os.urandom(16)
        encrypted = aes_cbc_encrypt(modified_input, random_key, iv)
    else:
        #do ecb
        encrypted = encrypt_block(pad(modified_input), random_key)
    return bytearray(encrypted)


def oracle(input):
    dict = Counter(chunks16(ret,1))
    return 'CBC' if not [v for k,v in dict.items() if v > 1] else 'ECB'

ret = encryption_oracle("A" * 16 * 4)

print oracle(ret)
print binascii.hexlify(ret)
