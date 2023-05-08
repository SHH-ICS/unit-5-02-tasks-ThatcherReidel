# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# Pword = input("Enter a word: ")
word = input("Enter a word: ")
length = len(word)

for i in range(length):
    print(word[:i+1])
    
for i in range(length-1, 0, -1):
    print(word[:i])