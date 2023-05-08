# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.
while True:
    word = input("Enter a word: ")
    if word == "quit":
        break
    print("Length of the word is", len(word))