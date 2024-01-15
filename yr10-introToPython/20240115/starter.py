import random
# Dog names array
dog_names = ["Buddy", "Max", "Charlie", "Lucy", "Sadie"]

# Tricks array
tricks = ["sit", "fetch", "roll over", "shake hands", "spin"]

# Simulate each dog performing a random trick
for dog_name in dog_names:
    # Randomly select a trick from the array - no errors on next line
    selected_trick = random.choice(tricks)

    # Perform the trick
    print(dog_name + " is doing the trick: "+selected_trick)

    # Selection: Check if the dog can do an additional trick based on a condition
    if selected_trick == "sit":
        print(dog_name+" can also lie down!")

    # Iteration: Repeat the trick a random number of times
    repeat_times = random.randint(1, 5)
    for i in range(repeat_times):
        print(dog_name+" does the trick again!")
