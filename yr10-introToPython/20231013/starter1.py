# Initialize a variable to keep track of whether the dog wants to go on a walk.
wants_to_walk = False

# Start a while loop to keep asking until the dog doesn't want to walk anymore.
while not wants_to_walk:
    user_input = input("Dog: Woof! Can we go for a walk? (yes/no): ")

    if user_input.lower() == "yes":
        print("You: Sure, let's go for a walk!")
        # You can add code here to simulate the walk or perform any desired actions.
        wants_to_walk = True
    else:
        print("You: Not now, maybe later.")
