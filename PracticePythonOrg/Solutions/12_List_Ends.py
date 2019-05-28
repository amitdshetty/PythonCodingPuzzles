"""
Problem statement

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""
import random
def addFirstandLastElementToNewList(b):
    c = []
    c.append(b[0])
    c.append(b[-1])
    print(c)

def main():
    isRandom = True
    if isRandom :
        a = random.sample(range(1,99),10)
        #a.sort()
    else:
        a = [5, 10, 15, 20, 25]
    print(a)
    addFirstandLastElementToNewList(a)

if __name__ == '__main__':
    main()