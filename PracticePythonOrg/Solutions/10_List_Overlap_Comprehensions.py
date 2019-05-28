"""
Problem Statement

This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

Extra:

Randomly generate two lists to test this

"""

import random

def main() :
    isRandom = True

    if isRandom :
        # List a allows for duplicates
        a = [random.randrange(1,99) for i in range(12)]
        # by default random.sample will not generate duplicates
        b = random.sample(range(1, 99), 18)
        # TBD : Cannot sort at the same time as creating the random list
        a.sort()
        b.sort()
    else :
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print('a = ' + str(a))
    print('b = ' + str(b))
    # Check with the smaller list first since it will lead to fewer initial iterations
    list_to_traverse = a if len(a) <= len(b) else b
    other_list_to_traverse = a if len(a) > len(b) else b
    # This will ensure only unique elements enter the list
    c = set()
    c = {d for d in list_to_traverse if d in other_list_to_traverse}

    print(c)

if __name__ == '__main__':
    main()