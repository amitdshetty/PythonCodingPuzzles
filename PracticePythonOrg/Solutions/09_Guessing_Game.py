"""
Problem Statement

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

def main() :
    min = 1
    max = 9
    count = 0
    print('Generating random number between ' + str(min) + ' and ' + str(max))
    randomNumber = random.randint(1,9)
    #print('The random number is ' + str(randomNumber))
    userGuess = str()
    while userGuess != 'exit':
        userGuess = input('Guess the number ...\n')
        count += 1
        if int(userGuess) < 0:
            print('Invalid Guess. Enter the correct format and try again')
        elif int(userGuess) > max :
            print("You're way off ....")
        else :
            if int(userGuess) > randomNumber :
                print('You went a little high. Try again')
            elif int(userGuess) < randomNumber :
                print('You went a little low. Try again')
            else :
                print ('You guessed it right. Congratulations. You guessed it in ' + str(count) + ' tries')
                break



if __name__ == '__main__':
    main()