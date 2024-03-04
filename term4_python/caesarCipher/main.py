asciiTable: list = [chr(i) for i in range(128)]

def encrypt (original: str, shift: int) -> str:
    rtrnString: str = ""
    for i in original:
        oldIndex: int = asciiTable.index(i)
        newIndex: int = oldIndex + shift
        newIndex -= 26
        if newIndex < 0:
             newIndex += 128
        elif newIndex > 128:
             newIndex -= 128
        rtrnString += asciiTable[newIndex]
    return rtrnString

def decrypt (encrypted: str, shift: int) -> str:
    rtrnString: str = ""
    for i in encrypted:
        oldIndex: int = asciiTable.index(i)
        newIndex: int = oldIndex - shift
        if newIndex < 0:
             newIndex += 128
        elif newIndex > 128:
             newIndex -= 128               
        rtrnString += asciiTable[newIndex]
    return rtrnString

def bruteforce (encrypted: str, commonLetter: str) -> str:
    mostLetter: int = 0
    largestN: int = 0
    for i in asciiTable:
        if encrypted.count(i) > largestN:
            mostLetter = asciiTable.index(i)
    for i in range(mostLetter, len(asciiTable)):
        if asciiTable[i] == commonLetter:
            shift = mostLetter - i
    for i in range(0, mostLetter):
         if asciiTable[i] == commonLetter:
            shift = mostLetter + i
    return decrypt(encrypted, shift)

func: str = input("Encrypt or Decrypt [e/d]? \n $ ")
if func.lower() == "e":
    inptString: str = input("What do you want to encrypt? \n $ ")
    inptShift: int = int(input("How much do you want to shift by? \n $ "))
    print(f"The encrypted string is\n {encrypt(inptString, inptShift)}")
elif func.lower() == "d":
    inptString: str = input("What do you want to decrypt? \n $ ")
    inptShift: int = int(input("How much is it shifted by? \n $ "))
    print(f"The decrypted string is\n {decrypt(inptString, inptShift)}")
elif func.lower() == "b":
    print(" --- Brute force mode --- ")
    inptString: str = input("What would you like to decode? \n $")
    print(f"Decoded string is: {bruteforce(inptString, 'e')}")