cipherInput: str = input("Blegh? ")
keyInput: int = int(input("Key?"))

def decipher(key, cipher):
    text: str = ""
    for i in range(0,len(cipher), key +1):
        text += cipher[i]
    return text

print(decipher(keyInput, cipherInput))
