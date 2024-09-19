'''
@ASSESSME.USERID: userID
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Mini Practicum
@ASSESSME.ANALYZE: YES
'''

import random

#Define constant for MINIMUM and MAXIMUM
MINIMUM = 1
MAXIMUM = 100

##Define constant for TOO_LOW, TOO_HIGH, CORRECT, YOU_WIN, OUT_OF_GUESSESS
TOO_LOW = "Too Low"
TOO_HIGH = "Too High"
CORRECT = "Correct"
YOU_WIN = "You Win!"
OUT_OF_GUESSES = "Out of Guesses!"

##Define function secret_number which generates numbers between MINIMUM and MAXIMUM
def secret_number():
    return random.randint(MINIMUM, MAXIMUM)

##Define function check_guess
def check_guess(secret, guess):
    if guess < secret:
        return TOO_LOW
    elif guess > secret:
        return TOO_HIGH
    else:
        return CORRECT

##Define function prompt_for_guess which implement a single guess
def prompt_for_guess():
    guess = int(input("Enter your guess: "))
    return guess

##Define function guessing_game
### - generate secret number
### - prompt 6 times
def guessing_game():
    secret = secret_number()
    attempts = 6
    
    while attempts > 0:
        guess = prompt_for_guess()
        result = check_guess(secret, guess)
        
        print(result)
        
        if result == CORRECT:
            print(YOU_WIN)
            break
        
        attempts -= 1
        if attempts == 0:
            print(OUT_OF_GUESSES)
            print(f"The secret number was: {secret}")

#Define main function
## Call the guessing game, and ask to play one more time!
def main():
    while True:
        guessing_game()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()