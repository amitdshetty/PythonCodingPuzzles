"""
Problem Statement

Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""
def splitAndJoinThis(userInput):
    splitThis = userInput.split()
    #splitThis.reverse()
    #result = " ".join(splitThis)
    print("String reversed by word " + " ".join(splitThis[::-1]))
    print("String reversed by alphabet " + userInput[::-1])

def main():
    userInput = input('Enter a sentence\n')
    print('You have entered',format(userInput))
    splitAndJoinThis(userInput)


if __name__ == '__main__':
    main()