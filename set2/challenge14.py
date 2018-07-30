#!/bin/python2
from challenge10 import aes_cbc_encrypt
from challenge10 import encrypt_block
from random import randrange
import os
import binascii
from collections import Counter
import random
import pprint
from base64 import b64decode
import json
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
random_key = os.urandom(16)

random_str = os.urandom(random.randint(1,16))

secret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\
        YnkK"

def chunks16(line):
    chunk_size = 16
    chunks = []
    so_far = 0
    while True:
        chunks.append(line[so_far:so_far+chunk_size])
        so_far += chunk_size
        if so_far >= len(line):
            break
    return chunks

def encryption_oracle(input):
    modified_input = random_str +  input + b64decode(secret)
    encrypted = encrypt_block(pad(modified_input), random_key)
    return bytearray(encrypted)


def oracle(input):
    dict = Counter([binascii.hexlify(i) for i in  chunks16(input)])
    return 'CBC' if not [v for k,v in dict.items() if v > 1] else 'ECB'


unknown_length = 0
for i in range(255):
    if 'ECB' == oracle(encryption_oracle("A" * i)):
        unknown_length = (16 - i % 16)
        print "The unknown random string has length: ", unknown_length
        break

itr = 16 * 9 - (1 + unknown_length)
pay = "A" * itr
dict = {}
decrypted = ""

while itr != 0:
    pay = "A" * itr
    for byte in range(0xff):
        cipher = encryption_oracle(pay + decrypted + chr(byte))
        chunks = chunks16(cipher)
        dict[binascii.hexlify(chunks[8])] = byte

    #print json.dumps(dict, indent=4)

    try:
        last_char = chr(dict[(binascii.hexlify(chunks16(encryption_oracle(pay))[8]))])
        #print last_char
        decrypted += last_char
    except:
        pass
    itr -= 1

print decrypted