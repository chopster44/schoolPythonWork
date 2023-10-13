dogsCount: int = int(input("How many dogs do you have? "))
dogsNames: list[str] = []
dogsAges: list[int] = []
for i in range(dogsCount):
    dogsNames.append(input("What is your dog's name? "))
    dogsAges.append(int(input(f"How old is {dogsNames[i]}? "))*7)

print(f"The oldest dog is {dogsNames[dogsAges.index(max(dogsAges))]}.")
print(f"The youngest dog is {dogsNames[dogsAges.index(min(dogsAges))]}.")
