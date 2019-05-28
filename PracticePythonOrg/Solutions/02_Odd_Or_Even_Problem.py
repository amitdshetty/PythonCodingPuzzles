"""
Problem Statement

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

import sys

def main():
    numberByUser = input('Enter the number \n') or "1"
    #print(numberByUser)
    # Or condition set a default value if user gives no input. Set it as 1 since we need to avoid divide by 0 errors
    numberCheck = input('Enter number you want check previous number with \n') or "1"
    if numberByUser :
        if numberCheck :
            if int(numberCheck) <= 0 :
                print("Application cannot check against 0. Try again...")
                sys.exit()
            if(int(numberByUser) % int(numberCheck) == 0) :
                print(numberByUser + " divides evenly with " + numberCheck)
            else :
                print(numberByUser + " does not divide evenly with " + numberCheck)
        else :
            if(int(numberByUser) % 4 ==0) :
                print(numberByUser + " is a multiple of 4")
            elif int(numberByUser) % 2 == 0 :
                print(numberByUser + " is even")
            else :
                print(numberByUser + " is odd")
    else :
        print('You have not entered any number to test with')

if __name__ == '__main__':
    main()