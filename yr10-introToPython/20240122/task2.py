file = open("Colours.txt", "w")
colours = ""
for i in range(0,8,1):
    colour = input("Enter a colour: ")
    colours += colour + " "

file.write(colours)
file.close()

file = open("Colours.txt", "r")
print(file.read())
