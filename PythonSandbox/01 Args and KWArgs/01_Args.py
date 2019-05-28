def callPrint3(*args) :
    print(f'The type of argument : {args} as {type(args)}')

# Using loops to call the dynamic arguments all at once
def callPrint2(*args):
    # for a in args:
    #     print(a)
    c = [a for a in args]
    print(c)


# Note: Despite variable arguments it will still give out of index errors
# Validate for every scenario of variable arguments
def callPrint1(*args):
    if(len(args) == 1):
        print(args[0])
    elif (len(args) > 1):
        print(args[0] + " " + args[1])
    else :
        pass

# Testing Dynamic arguments in python function calls
def callPrint(*args):
    for a in args:
        print(a)

def main():
    a = 'Amit'
    b = 'Shetty'
    c = 'Dharmapal'
    callPrint3(a,b,c)

if __name__ == '__main__':
    main()