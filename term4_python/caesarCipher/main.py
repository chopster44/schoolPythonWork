asciiTable: list = [chr(i) for i in range(128)]

def encrypt (original: str, shift: int) -> str:
    rtrnString: str = ""
    for i in original:
        oldIndex: int = asciiTable.index(i)
        newIndex: int = oldIndex + shift
        if i.isupper():
            if newIndex > 90:
                newIndex -= 26
        elif i.islower():
            if newIndex > 122:
                newIndex -= 26
        print(oldIndex, newIndex, asciiTable[newIndex])
        rtrnString += asciiTable[newIndex]
    return rtrnString

def decrypt (encrypted: str, shift: int) -> str:
    rtrnString: str = ""
    for i in encrypted:
        oldIndex: int = asciiTable.index(i)
        newIndex: int = oldIndex - shift
        if i.isupper():
            if newIndex < 65:
                newIndex += 26
        elif i.islower():
            if newIndex > 97:
                newIndex += 26
        print(oldIndex, newIndex, asciiTable[newIndex])
        rtrnString += asciiTable[newIndex]
    return rtrnString

func: str = input("Encrypt or Decrypt [e/d]? \n $ ")
if func.lower() == "e":
    inptString: str = input("What do you want to encrypt? \n $ ")
    inptShift: int = int(input("How much do you want to shift by? \n $ "))
    print(f"The encrypted string is\n {encrypt(inptString, inptShift)}")
elif func.lower() == "d":
    inptString: str = input("What do you want to decrypt? \n $ ")
    inptShift: int = int(input("How much is it shifted by? \n $ "))
    print(f"The decrypted string is\n {decrypt(inptString, inptShift)}")
