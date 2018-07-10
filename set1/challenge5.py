import binascii


def xor(msg, key):
    ret = bytearray()
    for i in range(len(msg)):
        ret.append(ord(msg[i]) ^ ord(key[i % len(key)]))
    return ret


m1 = "The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances."
print binascii.hexlify(xor(m1, "as0f8"))
