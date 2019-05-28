"""
Problem Statement

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

"""
# Use default value in the method argument incase no input is given from the call hierarchy
def getInputfromUser(userText = 'Please enter a number to check') :
    userText = userText + '\n'
    return int(input(userText))

# Check if number is prime if it is divisible upto half the user value a sthis will reduce the number of iterations
def checkIfPrime(numberGivenByUser):
    for i in range(2, int(numberGivenByUser/2)):
        if numberGivenByUser % i == 0:
            return False
    return True

def main():
    try :
        userInput = getInputfromUser()
        isPrime = checkIfPrime(userInput)
        if isPrime:
            print(str(userInput) + ' is a prime number')
        else:
            print(str(userInput) + ' is not prime')
    except ValueError as ve:
        print('Invalid input. ValueError exception thrown with the following message ' + str(ve))


if __name__ == '__main__':
    main()