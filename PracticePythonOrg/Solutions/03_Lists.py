"""
Problem Statement

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

"""

import sys

def main():
    inputByUser = int(input('Please enter a number to check \n') or '0')
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    try :
        indexHere = a.index(inputByUser)
    except ValueError :
        indexHere = -1
    #print(indexHere)
    if int(indexHere) == -1 :
        print('The number ' + inputByUser + ' is not present in the list ...')
        sys.exit()
    else :
        for number in a :
            if(number < int(inputByUser)) : b.append(number)
        print('There are no elements less than ' + str(inputByUser) if len(b) == 0 else b)

if __name__ == '__main__':
    main()