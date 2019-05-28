"""
Problem Statement

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random

# Returns list with duplicates removed
def removeDuplicatesFromList(x) :
    return list(dict.fromkeys(x))

#Solved problem statement using Python lists data structure
def performOperationWithList(a, b):
    c=[]
    # Check the smaller list first since it will save time
    list_to_check = a if len(a) <= len(b) else b
    other_list_to_compare = a if len(a) > len(b) else b
    for number in list_to_check:
        try:
            indexHere = other_list_to_compare.index(number)
        except ValueError:
            indexHere = -1
        if indexHere != -1:
            c.append(number)
    print(removeDuplicatesFromList(c))

#Solved problem statement using Python Sets and dict data structure
def performOperationWithSet(a, b):
    aSet = set()
    bSet = set()
    aSet = {d for d in a}
    bSet = {e for e in b}
    cSet = set()
    set_to_check = a if len(aSet) <= len(bSet) else bSet
    other_set_to_compare = aSet if len(aSet) > len(bSet) else bSet
    for number in set_to_check:
        if number in other_set_to_compare:
            cSet.add(number)
    print(cSet)

def main():

    isDynamic = True

    if isDynamic :
        # Dynamically generated random list
        # Functions used : random.sample(range of numbers, lenght of list to be genearted)
        a = random.sample(range(99), 12)
        b = random.sample(range(99), 12)
    else :
        # Static list initial test
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print("a : " + str(a) + "\nb : " + str(b))

    print("Performing Operation with Lists \n")
    performOperationWithList(a, b)

    print("\n")

    print("Performing Operation with Sets \n")
    performOperationWithSet(a, b)

if __name__ == '__main__':
    main()