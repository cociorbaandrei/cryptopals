import binascii

def xor(b1,b2):
    ret = bytearray()
    for i,j in zip(b1,b2):
        ret.append(ord(i) ^ ord(j))
    return ret

b1 = binascii.unhexlify("1c0111001f010100061a024b53535009181c")
b2 = binascii.unhexlify("686974207468652062756c6c277320657965")

print binascii.hexlify(xor(b1,b2))