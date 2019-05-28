"""
Problem Statement
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place,
they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many
“cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout
teh game and tell the user at the end.
"""
import random

def main():
    # To keep the game simple 4 digit number have been taken but it can be expanded to any number
    numberToGuess = generateRandomNumber()
    # numberToGuess = '1234'
    print(numberToGuess)
    numberToGuessArray = [int(i) for i in numberToGuess]
    numberEnteredByUser = input('Enter a number or type exit\n')
    if validateInput(numberToGuessArray, numberEnteredByUser):
        play_cow_and_bulls_game(numberToGuessArray, numberEnteredByUser)
    elif numberEnteredByUser.lower() == 'exit':
        print('You have decided to quit. Game is exiting now')
    else:
        print('Length of user input does not match the length to the number it is trying to match. User input should be of length {}'
              .format(len(numberToGuessArray)))

def generateRandomNumber():
    number = ''.join(map(str,random.sample(range(10),4)))
    print('Player has to guess {}'.format(number))
    return number

def validateInput(numberToGuessArray, numberEnteredByUser):
    if len(numberEnteredByUser) == len(numberToGuessArray):
        return True
    return False

def play_cow_and_bulls_game(numberToGuessArray, numberEnteredByUser):
    """
    Function returns the numbers of cows and bulls based on the game logic
    :param numberToGuessArray:
    :return:
    """
    while numberEnteredByUser.lower() != 'exit':
        i = 0
        cows = 0
        bulls = 0
        for j in range(len(numberEnteredByUser)):
            if int(numberEnteredByUser[i]) == int(numberToGuessArray[i]):
                cows += 1
            elif int(numberEnteredByUser[i]) in numberToGuessArray:
                bulls += 1
            i += 1
        if cows == len(numberEnteredByUser):
            break
        else:
            print('You have {} cow(s) and {} bull(s)'.format(cows, bulls))
            numberEnteredByUser = input('Try again. Enter a number or type exit\n')
            if validateInput(numberToGuessArray, numberEnteredByUser) == False:
                print('Length of user input does not match the length to the number it is trying to match. User input should be of length {}'.format(
                        len(numberToGuessArray)))
                break

if __name__ == '__main__':
    main()