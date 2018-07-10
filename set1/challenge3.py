import binascii

english_freq = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,  # A-G
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,  # H-N
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,  # O-U
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074                     # V-Z
]


# msg is expected as raw binary
def xor(msg, key):
    ret = bytearray()
    for i in msg:
        ret.append(ord(i) ^ key)
    return ret

# msg is expected as raw binary
def get_score(msg):
    count = [] 
    ignored = 0
    for i in range(26):
        count.append(0)

    for i in msg:
        c = i
        if (c >= 65 and c <= 90):
            count[c - 65] += 1
        elif (c >= 97 and c <= 122):
            count[c - 97] += 1
        elif (c >= 32 and c <= 126):
            ignored += 1
        elif c == 9 or c == 10 or c == 13:
            ignored += 1
        else:
            return 0xfffffff

    chi2 = 0 
    l = len(msg) - ignored

    for i in range(26):
        observed = count[i]
        expected = l * english_freq[i]
        difference = observed - expected
        chi2 += difference*difference / expected

    return chi2

to_crack = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
sol = "Cooking MC's like a pound of bacon"


messages = []
for i in range(0xFF):
    m = xor(to_crack, i)
    messages.append((m, get_score(m)))


for msg in sorted(messages, key=lambda x: x[1]):
    print msg