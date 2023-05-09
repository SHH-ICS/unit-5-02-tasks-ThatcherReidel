# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# Pword = input("Enter a word: ")
word = input("Please enter a word: ")
for i in range(len(word)):
    print(word[:i+1])