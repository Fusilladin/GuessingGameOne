# GUESSING GAME ONE
import random


r = random.randint(1, 9)
guess = 0

while True:
    x = (int(input('Guess the number from 1-9  ')))
    guess+=1
    if x > r:
        print('You guessed too high, try again.')
        print(x)
        continue
    if x < r:
        print('You guessed too low, try again.')
        print(x)
        continue
    if x == r:
        print('You guessed {} correctly! It took you {} tries'.format(r, guess))
        break


# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly rTight. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
