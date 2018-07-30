
import re
from random import randrange
import os
import binascii
from challenge10 import encrypt_block
from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s : s[:len(s) - ord(s[len(s) - 1])]
RANDOM_KEY = os.urandom(16)

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

def parse_cookie(cookie):
    parsed = {}
    for keyvalue in cookie.split("&"):
        keypair = keyvalue.split("=")
        parsed[keypair[0]] = keypair[1]
    return parsed

def encode_dictionary(dictionary):
    encoded = "email={email}&uid={uid}&role={role}".format(
        email=dictionary['email'],
        uid=dictionary['uid'],
        role=dictionary['role'])
    return encoded

def profile_for(email):
        user_profile = {}
        user_profile["email"] = email
        user_profile["uid"]  = 10
        user_profile["role"] = "user"
        return encode_dictionary(user_profile)


def encrypt_profile(input):
    modified_input = input
    encrypted = encrypt_block(pad(modified_input), RANDOM_KEY)
    return bytearray(encrypted)

def decrypt_profile(input):
    cipher = AES.new(RANDOM_KEY, AES.MODE_ECB)
    return (cipher.decrypt(buffer(input)))

if __name__ == '__main__':
    print binascii.hexlify(RANDOM_KEY)
    payload = "AAAAAAAAAA"
    payload += pad("admin")
    payload += "A" * 11
    payload +="cociorbaandrei@gmail.com"

    encoded = profile_for(payload)

    crypted = encrypt_profile(encoded)

    for line in chunks16(crypted):
        print binascii.hexlify(line), decrypt_profile(line)

    decrypted = decrypt_profile(crypted)
    parsed = parse_cookie(decrypted)

    print unpad(decrypted)
    chunks = chunks16(crypted)
    
    new_cipher = ""
    new_cipher += chunks[0]
    new_cipher += chunks[1]
    new_cipher += chunks[2]
    new_cipher += chunks[3]
    new_cipher += chunks[4]
    new_cipher += chunks[1] # swap user||PADDING block with admin||PADDING 

    print "Tampered:"
    print unpad(decrypt_profile(new_cipher))
    
    