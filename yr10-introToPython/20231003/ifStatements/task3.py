word: str = str(input("Input your word"))
if word[::-1] == word:
    print("Is a palendrome")
else:
    print("not a palendrome")