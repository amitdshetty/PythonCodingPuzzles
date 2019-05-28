"""
Problem Statement
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
"""
def main():
    numbers_list = [20,32,43,56,15,76,99]
    # Sorting random numbers in ascending
    numbers_list.sort()
    print(numbers_list)
    #check_number(numbers_list)
    # Performing same operation using binary search
    low, high = 0, len(numbers_list) - 1
    number_to_check = int(input('Enter a number to check\n'))
    is_present = perform_binary_search(numbers_list, number_to_check, low, high)
    if is_present:
        print('Number found')
    else:
        print('Number not found')

def perform_binary_search(numbers_list, number_to_check, low, high):
    """
    TBD since it can only find numbers but fails if it doesn't find one
    :param numbers_list:
    :param number_to_check:
    :param low:
    :param high:
    :return:
    """
    is_present = False
    mid = int((low + high) / 2)
    numbers_list_2 = list(map(int, numbers_list))
    if number_to_check == numbers_list_2[mid]:
        is_present = True
        return is_present
    elif number_to_check < numbers_list_2[mid]:
        # perform binary search from 0 to mid-1
        is_present = perform_binary_search(numbers_list_2, number_to_check, 0, mid - 1)
    else:
        # perform binary search from mid+1 to high
        is_present =  perform_binary_search(numbers_list_2, number_to_check, mid+1, high)
    return is_present

def check_number(numbers_list):
    while True:
        number_to_check = int(input('Enter a number to check\n'))
        is_present = number_to_check in numbers_list
        if is_present:
            print('{} is present in the list'.format(number_to_check))
            break
        else:
            print('{} is not present in the list'.format(number_to_check))


if __name__ == '__main__':
    main()