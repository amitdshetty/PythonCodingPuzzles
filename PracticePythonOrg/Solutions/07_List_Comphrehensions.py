"""
Problem Statement

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a
and makes a new list that has only the even elements of this list in it.

"""

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print("Input \n" + str(a))
    # b = []
    # for numbers in a:
    #     if numbers % 2 == 0 :
    #         b.append(numbers)

    # The for loop and conditional check has been compressed to a single line
    b = [numbers for numbers in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] if(numbers % 2 == 0)]

    # Playing around with comprehensions
    # Play 1 : Nested For Loops and check for numbers divisible by 3
    b1 = [[c,d] for c in a for d in a if d % 3 == 0]

    # Play 2 : Squares of numbers
    b2 = [ c**2 for c in a]

    # Play 3 : Squares and cubes at the same time for the same array
    b3 = [(c ** 2,c ** 3) for c in a]

    print("\nEven numbers")
    print(b)

    print("\nNested For Loops and check for numbers divisible by 3")
    print(b1)

    print("\nSquares of numbers")
    print(b2)

    print("\nSquares and cubes at the same time for the same array")
    print(b3)

if __name__ == '__main__':
    main()