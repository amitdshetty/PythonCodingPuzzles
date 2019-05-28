"""
Problem Statement
In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you,
the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle
of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!
(We’ll talk about what is the optimal one next week with the solution.)

"""
import random

def main():
    number_to_guess = 78
    guess_the_number(number_to_guess)


def guess_the_number(number_to_guess, low = 0, high = 100, iter = 0):
    """
    Function uses recursion to guess a number given by the user which the former is unaware of
    One way to improve this function is that instead of only passing the low or high values in the recursive calls
    we can set them both up in such a way that the low or high value can be the 'number_to_guess' variable + 1 to lower the range
    further but it will overly complicate the problem
    :param number_to_guess:
    :param low:
    :param high:
    :param iter:
    :return:
    """
    current_guess = random.randint(low, high+1)
    i = iter + 1
    print('Current Guess #{} : {}'.format(i, current_guess))
    if current_guess == number_to_guess:
        print('Number has been identified correctly in {} steps'.format(i))
    elif current_guess < number_to_guess:
        # Goal is to reduce range form where the application can take a random guess
        guess_the_number(number_to_guess, low = current_guess, iter = i)
    else :
        # Goal is to reduce range form where the application can take a random guess
        guess_the_number(number_to_guess, high = current_guess, iter = i)

if __name__ == '__main__':
    main()