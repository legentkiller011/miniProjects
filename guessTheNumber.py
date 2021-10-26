# you should guess a number between 1-10 and it your guess is right, you will get points. if not, you'll lose pints.
# if you run out of points, you will lose. if you have 10 scores, you will win.

import random
import sys

# takes input
life = input("\n\nplease enter the amount of your lives \n")

# error handling when the input is not int
try:
    lives = int(life)

except ValueError:
    print("\n please try again entering a valid number!")
    sys.exit(0)


while lives > 0:
    guessedNumber = input("please guess a number \n")

    # error handling when the input is not int
    try:
        guessed = int(guessedNumber)

    except ValueError:
        print("\n please try again entering a valid number!")
        sys.exit(0)

    # create random number
    randomNumber = random.randint(0, 10)

    # comparing the numbers
    if guessed == randomNumber:
        print("congratz! you guessed right! the number is: " + str(randomNumber) + "\n")
        print("you have " + str(lives) + "lives.")

    else:
        lives -= 1

        print("sorry! the correct number is: " + str(randomNumber) + "\n \nfor that you lose a life. your new life is now reduced to " + str(lives))
# running out of lives (Game Over)
else:
    print("you now have lost all of your lives, therefore you lose!")


