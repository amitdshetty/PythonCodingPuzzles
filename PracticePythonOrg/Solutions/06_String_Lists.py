"""
Problem Statement

Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

"""

def main():
    try:
        stringInputByUser = input("Enter the string to check if it is a palindrome or not \n")

        #Print a string from the reverse from the last index to the first
        reverseStringInputByUser = stringInputByUser[::-1]
        print("Reversed String by user is " + reverseStringInputByUser)
        #
        # if(stringInputByUser.lower() == reverseStringInputByUser.lower()) :
        #     print(stringInputByUser + " is a palindrome")
        # else:
        #     print(stringInputByUser + " is not a palindrome")

        print(stringInputByUser + " is a palindrome" if stringInputByUser.lower() == reverseStringInputByUser.lower()
              else stringInputByUser + " is not a palindrome")
    except ValueError as ve:
        print("Invalid input. ValueError has been thrown with the following message ==> " + str(ve))


if __name__ == '__main__':
    main()