"""EX03 - Complete Wordle."""

__author__ = "730489799"
# Create global variables for emojis and secret_Word
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "codes"


def contains_char(word: str, letter: str) -> bool:
    """Create function to check if a given letter exists in a word."""
    assert len(letter) == 1
    output: bool = False
    word_len: int = len(word)
    counter: int = 0

    while counter < word_len:
        if word[counter] == letter:
            output = True
        counter += 1
    
    return output


def emojified(guess: str, secret: str) -> str:
    """Compares the guessed word from the user and the secret word to determine whether each letter in the guessed word is in secret_word, and whether it is in the correct position. Then print the corresponding emojis to the user."""
    assert len(guess) == len(secret)
    guess_len: int = len(guess)
    output: str = ""
    counter: int = 0

    while counter < guess_len:
        if guess[counter] == secret[counter]:
            output += GREEN_BOX
        elif contains_char(secret, guess[counter]):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        counter += 1
    return output


def input_guess(exp_length: int) -> str:
    """Prompt user for input, if the input is of an incorrect length kept prompting until the correct length word is inputted."""
    guess: str = input(f"Enter a { exp_length } character word: ")
    while len(guess) != exp_length:
        guess = input(f"That wasn't { exp_length } chars! Try again: ")
    
    return guess


def main() -> None:
    """The entrypoint of the program and the main loop."""
    turn_num: int = 0
    total_turns: int = 6
    has_not_won: bool = True

    while turn_num < total_turns and has_not_won:
        turn_num += 1
        print(f"=== Turn {turn_num}/{total_turns} ===")
        user_guess: str = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            has_not_won = False
            print(f"You won in { turn_num }/{ total_turns } turns!")
    
    if turn_num >= total_turns:
        print(f"X/{total_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()