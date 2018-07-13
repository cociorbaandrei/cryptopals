
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

def parse_cookie(cookie):
    parsed = {}
    for keyvalue in cookie.split("&"):
        keypair = keyvalue.split("=")
        parsed[keypair[0]] = keypair[1]
    return parsed

def valid_email(email):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

def encode_dictionary(dictionary):
    encoded = ""
    count = 0
    for key, value in sorted(dictionary.iteritems()):
        encoded += str(key) + "=" + str(value)
        count += 1
        if(count != len(dictionary)):
            encoded += "&"
    return encoded

def profile_for(email):
    if(not valid_email(email)):
        raise Exception("Invalid email address!")
    else:
        user_profile = {}
        user_profile["email"] = email
        user_profile["uid"]  = randrange(1,1000)
        user_profile["role"] = "user"
        return (user_profile)


def encrypt_profile(input):
    modified_input = input
    encrypted = encrypt_block(pad(modified_input), RANDOM_KEY)
    return bytearray(encrypted)

def decrypt_profile(input):
    cipher = AES.new(RANDOM_KEY, AES.MODE_ECB)
    return (cipher.decrypt(buffer(input)))

if __name__ == '__main__':
    print binascii.hexlify(RANDOM_KEY)
    print parse_cookie("foo=bar&baz=qux&zap=zazzle")
    profile = profile_for("cociorbaandrei@gmail.com")
    encoded = encode_dictionary(profile)
    crypted = encrypt_profile(encoded)
    hex_crypted = binascii.hexlify(crypted)
    decrypted = decrypt_profile(crypted)
    parsed = parse_cookie(decrypted)
    print hex_crypted
    print parsed
    