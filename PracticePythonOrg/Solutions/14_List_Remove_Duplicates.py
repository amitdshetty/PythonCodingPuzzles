"""
Problem Statement

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""
def doUsingLoop(a):
    b = []
    for number in a:
        if number not in b:
            b.append(number)
    print(b)

def doUsingSet(a):
    # Converting list to set
    b = set(a)
    #b = {number for number in a}
    print(b)

def main():
    a = [1,1,2,3,5]
    doUsingLoop(a)
    doUsingSet(a)

if __name__ == '__main__':
    main()