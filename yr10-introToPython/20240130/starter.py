# Write a program to count the number of words in a sentence stored in a file
# • Create a file that stores a sentence - e.g. The quick brown fox jumps over the lazy dog
# • The program should respond with the number of words in the sentence
# • Hint - look for spaces and full stops in the string
# Can you build on the program to print the sentence backwards?

fileName = input("What file would you like to count? ")

file = open(fileName, "r")

text = file.read()

numWords = len(text.split(" "))

print(f"There are {numWords} words in {fileName}")

