"""EX02 - One Shot Wordle"""

__author__ = "730489799"
# Add variables for emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#Define variables for the word to be guessed and its length
secret_word: str = "python"
word_length: int  = len(secret_word)
# Prompt user with initial guess language
guess: str = input(f"What is your { word_length }-letter guess? ")
# Intialize empty string to store the emojis to be outputted to the user
emoji_result: str = ""
# Intialize iterator for comparing the guessed word and secret word
str_index: int = 0

# We want to continue prompting for guesses if the guess is incorrect or the guessed word is of an incorrect length
while guess != secret_word or len(guess) != word_length:
    # Check if the guess is the right length and that it is not the secret word
    if (len(guess) == word_length and guess != secret_word):
        # Iteratre through the guessed word and secret word to compare invidiual letters
        while str_index < word_length:
            # If the letter is in the correct index add a green box to the output
            if guess[str_index] == secret_word[str_index]:
                emoji_result += GREEN_BOX
            # If the letter is not in the correct place, there are two possibilities: it is a letter that doesn't appear in the secret word
            # or its a letter that is in the secret word but is in the wrong index in the current guess
            else:
                exists: bool = False
                check_index: int = 0
                # Iterate through the secret word and see if the current letter exists in the word, if it does the loop will break
                while check_index < word_length and exists == False:
                    if guess[str_index] == secret_word[check_index]:
                        exists = True
                    check_index += 1
                # If the letter exists elsewhere in the word add a yellow box, otherwise add a white box
                if exists:
                    emoji_result += YELLOW_BOX
                else:
                    emoji_result += WHITE_BOX
            #emoji_result += " "
            # Increment counter for overall iterator going through the guessed and secret word
            str_index += 1
        # Print emoji string with boxes and exit because the guess was incorrect as we check above
        print(emoji_result)
        print("Not quite! Play again soon!")
        exit()
    
    else:
        # If the guessed word was not of the right length, we prompt the user again with the guess variable
        guess = input(f"That was not { word_length } letters! Try again: ")
# If the program didn't exit with an incorrect guess of the correct length, it means that the guess was correct and thus
# the control flow will come here and pring the green boxes and the success message
print(word_length * GREEN_BOX)
print("Woo! You got it!")