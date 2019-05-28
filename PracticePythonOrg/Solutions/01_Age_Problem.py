"""
Problem Statement

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""


from datetime import date
import sys

# Returns the year in which the user turned 100
def getYearWhen100(currentYear, yearsCrossedSince100):
    return currentYear - yearsCrossedSince100

def main():
    name = input('Enter your name \n')
    # print(name)
    age = int(input('Enter your age \n') or int(0))
    # print(age)
    today = date.today()
    currentYear = today.year
    # print(currentYear)
    noOfTimesToPrint = int(input('Enter the number of time you would like to print this message \n'))
    print(name + ', you are ' + str(age) + ' years old in ' + str(currentYear))
    if age > 100:
        print(noOfTimesToPrint * (
                    'You are already over 100. You turned 100 back in ' + str(getYearWhen100(currentYear, age - 100)) + "\n"))
        sys.exit()
    else:
        yearsLeftToTurn100 = 100 - age
        # Subtracting 1 since it will given year after turning 100 as the answer
        yearTurning100 = (currentYear + yearsLeftToTurn100) - 1
        print(noOfTimesToPrint * (name + ', you will turn 100 in ' + str(yearTurning100) + "\n"))

if __name__ == '__main__':
    main()
