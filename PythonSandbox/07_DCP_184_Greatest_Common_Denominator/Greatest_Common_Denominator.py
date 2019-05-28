"""
Problem Statement:
This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

def main():
    user_input = [24, 40, 42]
    lowest = min(user_input)
    if check_input_first(user_input, lowest):
        print('GCD is {}'.format(lowest))
    else:
        print('GCD is not in input. Checking other options...')
        max = check_other_options(user_input, lowest)
        if max > 0:
            print('GCD is {}'.format(max))
        else:
            print('GCD cannot be found')


def check_input_first(user_input, lowest):
    flag = False
    for i in user_input:
        if i % lowest == 0:
            flag = True
        else:
            flag = False
            break
    return flag

def check_other_options(user_input, lowest):
    flag = False
    max = 0
    for j in range(2, lowest):
        for k in user_input:
            if k%j == 0:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            max = j
    return max

if __name__ == '__main__':
    main()