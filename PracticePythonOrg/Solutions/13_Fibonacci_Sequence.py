"""
Problem Statement

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def fibonacci(number):
    result = []
    first = 0
    second = 1
    for i in range(number):
        first, second = second, first+second
        result.append(first)
    print(result)

def main():
    userInput = int(input('Enter the number of steps for fibonacci to be performed\n'))
    fibonacci(userInput)

if __name__ == '__main__':
    main()