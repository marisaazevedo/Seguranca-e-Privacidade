from binascii import hexlify, unhexlify
from calculate_prime import nextPrime
from find_d import mod_inverse

p = nextPrime(2 ** 512)
q = nextPrime(2 ** 513)
n = p * q
e = 0x10001 # a constant
d = mod_inverse(e, (p - 1) * (q - 1))

enc_flag = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000023ddceba2c6e9209ead7434cc615b02eae15067765ebaf0a15b17234a300acee84ac1ddedefddc03d36d2f2bb16b6f9895e760f6f1a365c9487d3928630ecce9f12c0019ff66f02cce2b2715175b2aee2a3fc997bdaabc8d6d54b0b73972af8dfdc3b25c4e8b17c4c5729c5195c9f3586f5ee607a53418575362b2e06c065d32"

def enc(x):
    int_x = int.from_bytes(x, "big")
    y = pow(int_x, e, n)
    return hexlify(y.to_bytes(256, 'big'))

def dec(y):
    int_y = int.from_bytes(unhexlify(y), "big")
    x = pow(int_y, d, n)
    return x.to_bytes(256, 'big')

y = dec(enc_flag)
print(y.decode())
