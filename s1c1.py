import base64
import binascii

str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
str_as_hex = binascii.unhexlify(str)
str_as_b64 = base64.b64encode(str_as_hex).decode("utf8")
print(str_as_b64)
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
