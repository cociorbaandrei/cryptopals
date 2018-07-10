#!/bin/python2

"""
openssl enc -d -a -aes-128-cbc -K 41414141414141414141414141414141 -iv 00000000000000000000000000000000  -in <(echo -e $(python2 challenge9.py))
"""
import binascii
import base64
from Crypto.Cipher import AES
from base64 import *

def xor(msg, key):
    ret = bytearray()
    for i in range(len(msg)):
        ret.append((msg[i]) ^ ord(key[i % len(key)]))
    return ret

def read_file():
    return b64decode(open("7.txt", "rb").read())


def encrypt_block(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)

def decrypt_block(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(msg)

def pad(msg, l):
    padding = chr(l - len(msg)) * (l - len(msg))
    return bytearray(msg + padding)


def aes_cbc_encrypt(msg, key, iv = None):
    block_size = 16
    so_far = 0
    if iv == None:
        iv = "\x00" * block_size
    previous_cipher = iv
    crypted = bytearray()
    while True:
        curent_block = pad(msg[so_far:so_far + block_size], 16)
        #print curent_block
        xored_block = xor(curent_block, previous_cipher)
        cipher = encrypt_block(buffer(xored_block),key)
        previous_cipher = cipher
        crypted += cipher
        so_far += 16
        if so_far >= len(msg):
            break
    return crypted

print base64.b64encode( aes_cbc_encrypt("MUIE DRAGNEA MUIE CUrvo", "A" * 16))

    
