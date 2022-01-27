"""EX02 - One Shot Wordle"""

__author__ = "730489799"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
word_length: int  = len(secret_word)

guess: str = input(f"What is your { word_length }-letter guess? ")
emoji_result: str = ""
str_index: int = 0

while guess != secret_word or len(guess) != word_length:
    if (len(guess) == word_length and guess != secret_word):
        while str_index < word_length:
            if guess[str_index] == secret_word[str_index]:
                emoji_result += GREEN_BOX
            else:
                exists: bool = False
                check_index: int = 0
                while check_index < word_length and exists == False:
                    if guess[str_index] == secret_word[check_index]:
                        exists = True
                    check_index += 1
                
                if exists:
                    emoji_result += YELLOW_BOX
                else:
                    emoji_result += WHITE_BOX
            #emoji_result += " "
            str_index += 1
        print(emoji_result)
        print("Not quite! Play again soon!")
        exit()
    
    else:
        guess = input(f"That was not { word_length } letters! Try again: ")

print(6 * GREEN_BOX)
print("Woo! You got it!")