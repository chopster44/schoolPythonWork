import random
# List of treats
treats = ["Chocolate cake", "Fruit salad", "Ice cream", "Cookies", "Yogurt"]

# Assume the user has eaten all their vegetables (you can modify this condition)
has_eaten_vegetables = input("Have you eaten all your vegtables?")

def get_treat(treat_list):
    num = random.randint(0,len(treat_list))
    chosen_treat = treat_list[num]
    print("Congratulations! You've earned a " +chosen_treat+" for dessert.")
    want = input("Do you want this treat?")
    if want == "no":
        new_treat_list = treat_list[:]
        new_treat_list.remove(chosen_treat)
        get_treat(new_treat_list)
    else:
        return

if has_eaten_vegetables=="yes":
    get_treat(treats[:])
else:
    print("Remember to eat your vegetables first!")

