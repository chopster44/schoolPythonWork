import random
num = random.randint(1, 4)
item = ""
if num == 1:
    item = "sword"
elif num == 2:
    item = "hammer"
elif num == 3:
    item = "lucky gold"
elif num == 4:
    item = "sack of potatoes"

print("You have collected ", item)
print("You come across an ogre")
fight = input("Do you fight?")
if fight == "yes":
    if (item == "sword" or item == "hammer"):
        print("You win the fight!")
    elif item == "lucky gold":
        print("You are lucky he was a friendly ogre")
    else:
        print("You are dead")
elif fight == "no":
    if item == "sack of potatoes":
        print("Too late, the ogre is after your potatoes")
    else:
        print("You live another day")
else:
    print("Your incorrect input means that the ogre is after you and you lose your item")
    item = ""
