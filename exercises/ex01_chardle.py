"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730489799"

five_let_word: str = input("Enter a 5-character word: ")
if len(five_let_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + five_let_word)
counter: int = 0
if five_let_word[0] == character:
    print(character + " found at index 0")
    counter += 1
if five_let_word[1] == character:
    print(character + " found at index 1")
    counter += 1
if five_let_word[2] == character:
    print(character + " found at index 2")
    counter += 1
if five_let_word[3] == character:
    print(character + " found at index 3")
    counter += 1
if five_let_word[4] == character:
    print(character + " found at index 4")
    counter += 1

if counter == 0:
    print("No instances of " + character + " found in " + five_let_word)

elif counter == 1:
    print(str(counter) + " instance of " + character + " found in " + five_let_word)

else:
    print(str(counter) + " instances of " + character + " found in " + five_let_word)