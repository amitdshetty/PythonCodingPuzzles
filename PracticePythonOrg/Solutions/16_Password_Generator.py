"""
Problem Statement

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random
import sys

def main():
    """
    In order to pick a random work we must first prepare the following things
    a. List of all upper case letters
    b. List of all lower case letters
    c. List of numbers from 0-9
    d. List of special characters

    Apprach : Using ASCII number in conjunction with chr function of Python
    """

    print("Password Generator Service")
    # If no input is given by user then the maximum length password is genearted
    lengthOfPassword = int(input("Enter length of password (8 or greater) or leave blank to generate a password of maximum length i.e. 77 characters\n") or int(77))
    # Additional Input Validation
    if lengthOfPassword < 8 or lengthOfPassword > 77:
        print("Invalid Entry. Enter a value that is 8 or greater and less than 77 characters as they make secure passwords. Please try again")
        sys.exit()

    upperCaseLowerLimit = 65
    upperCaseUpperLimit = 90

    lowerCaseLowerLimit = 97
    lowerCaseUpperLimit = 122

    specialSymbolsLowerLimit = 33
    specialSymbolsUpperLimit = 47

    upperCaseList = [chr(i) for i in range(upperCaseLowerLimit, upperCaseUpperLimit + 1)]
    lowerCaseList = [chr(i) for i in range(lowerCaseLowerLimit, lowerCaseUpperLimit + 1)]
    specialSymbolsList = [chr(i) for i in range(specialSymbolsLowerLimit, specialSymbolsUpperLimit + 1)]
    numbersList = [i for i in range(0,10)]

    """
    To generate random characters of even greater length the list might have to be duplicated
    This has not be done now due to practical reasons.
    Sample code for doing so can be seen below
    random.sample(upperCaseList*2, len(upperCaseList)*2)
    """
    possibleSymbols = random.sample(upperCaseList, len(upperCaseList)) + random.sample(lowerCaseList, len(lowerCaseList)) \
                      + random.sample(specialSymbolsList, len(specialSymbolsList)) + random.sample(numbersList, len(numbersList))
    # the core functionality that determines the complex password
    random.shuffle(possibleSymbols)

    finalPassword = ''.join(str(s) for s in possibleSymbols[:lengthOfPassword])

    print("Your new password of length {} is generated ==> {}".format(lengthOfPassword, finalPassword))

if __name__ == '__main__':
    main()