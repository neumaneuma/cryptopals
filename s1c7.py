from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

key = b"YELLOW SUBMARINE"

with open("7.txt") as input_file:
    ciphertext = base64.b64decode(input_file.read())

cipher = Cipher(algorithms.AES(key), modes.ECB())
# encryptor = cipher.encryptor()
# ct = encryptor.update(b"a secret message") + encryptor.finalize()
# decryptor = cipher.decryptor()
# decryptor.update(ct) + decryptor.finalize()
decryptor = cipher.decryptor()
plaintext = (decryptor.update(ciphertext) + decryptor.finalize()).decode("utf8")
print(plaintext)