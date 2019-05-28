# Using the dynamic dictionary to retrieve specific key value pairs
def callPrint3(key, **kwargs):
    # Get dictionary keys
    print(kwargs.get(key))
    # Get dictionary key value pairs
    for oneKey,value in kwargs.items():
        print(oneKey + " " + value)

# Define both the key and value to specify which argument to use
# Prevents the need for method overloading
def callPrint2(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} and {value}')

# Shows how a dictionary is used to pass dynamic key value paors to the function
def callPrint(**kwargs):
    print(f'The Arguemnt here are {kwargs} as {type(kwargs)}')

def main():
    a = 'Amit'
    b = 'Shetty'
    callPrint3('test1', test1 = a, test2 = b)

if __name__ == '__main__':
    main()