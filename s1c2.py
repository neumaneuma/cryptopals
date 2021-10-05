import binascii
import sys

a = "1c0111001f010100061a024b53535009181c"
a2 = binascii.unhexlify(a)

b = "686974207468652062756c6c277320657965"
b2 = binascii.unhexlify(b)

bo = sys.byteorder
c = int.from_bytes(a2, bo) ^ int.from_bytes(b2, bo)
xor_length = max(len(a2), len(b2))
c2 = c.to_bytes(xor_length, bo)
c3 = binascii.hexlify(c2).decode("utf8")
print(c3)
# 746865206b696420646f6e277420706c6179
