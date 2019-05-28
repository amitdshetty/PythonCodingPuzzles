"""
Problem Statement

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13
has no remainder.)

"""

import sys

def main() :
    try:
        inputByUser = int(input('Enter the number to check divisors for \n' or '1'))
        divisors = []
        if inputByUser <= 0 :
            print('Please enter a valid input ... ')
            sys.exit()
        elif inputByUser == 1 :
            print('The only divisor for 1 is 1')
            sys.exit()
        else :
            # 1 is added so that it includes itself as a divisor which is a valid result
            for i in range(1,inputByUser + 1):
                if inputByUser % i == 0 :
                    divisors.append(i)
        print('There are no divisors for ' + str(inputByUser) if len(divisors) == 0 else divisors)
    except ValueError as ve:
        print('Invalid input format. ValueError Exception raised with message ==> ' + str(ve))
        sys.exit()


if __name__ == '__main__':
    main()