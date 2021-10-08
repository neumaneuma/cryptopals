str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
str_as_bytes = bytes.fromhex(str)

potential_keys = [i for i in range(0, 128)]
potential_messages = []
for key in potential_keys:
    m = []
    for byte in str_as_bytes:
        m.append(bytes([byte ^ key]))
    message = b''.join(m)

    potential_messages.append(message)
    
# Just trying to brute force it instead of the fancy letter frequency trick since that's not necessary for me to understand the crypto behind this
for i, m in enumerate(potential_messages):
    try:
        print(f"{i}: {m.decode().rstrip()}")
    except UnicodeDecodeError as e:
        print(f"{i}: UnicodeDecodeError")
