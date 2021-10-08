import sys

a = "1c0111001f010100061a024b53535009181c"
a2 = bytes.fromhex(a)

b = "686974207468652062756c6c277320657965"
b2 = bytes.fromhex(b)


bo = sys.byteorder
c = int.from_bytes(a2, bo) ^ int.from_bytes(b2, bo)
xor_length = max(len(a2), len(b2))
c2 = c.to_bytes(xor_length, bo)
c3 = bytes.hex(c2)
print(c3)
# 746865206b696420646f6e277420706c6179

# This is how to do it without converting to and from bytes (much simpler)
d = int(a, 16)
e = int(b, 16)
print(hex(d ^ e))