# Write a program that allows the user to input the names of various zoo animals and store them in an array.
# Once the animals are stored, use a loop to iterate through the array and count the total number of animals in the zoo. 
# Finally, print out the total count of animals in the zoo.
zooAnimals: list[str] = []
while True:
    tempAnimal: str = str(input("Add an animal (q to exit) $ "))
    if tempAnimal == "q":
        break
    else:
        zooAnimals.append(tempAnimal)

printStatement: str = "You have "
printStatement += str(len(zooAnimals))
printStatement += " animals"
print(printStatement)
