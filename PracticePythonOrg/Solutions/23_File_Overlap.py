"""
Problem Statement:
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics -
you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
"""

def main():
    prime_number_file_location = '/Users/amitshetty/Desktop/primenumbers.txt'
    happy_numbers_file_location = '/Users/amitshetty/Desktop/happynumbers.txt'

    prime_numbers_list = read_and_add_to_list(prime_number_file_location)
    happy_numbers_list = read_and_add_to_list(happy_numbers_file_location)

    print('File Stats -> \nPrime Numbers: {}, Happy Numbers: {}'.format(len(prime_numbers_list), len(happy_numbers_list)))

    if len(prime_numbers_list) < len(happy_numbers_list):
        calculate_file_overlap(prime_numbers_list, happy_numbers_list)
    else:
        calculate_file_overlap(happy_numbers_list, prime_numbers_list)

def calculate_file_overlap(smallest_list, largest_list):
    file_overlap_list = [int(number) for number in smallest_list if number in largest_list]
    print('Numbers common to both lists ==>\n{}'.format(file_overlap_list))



def read_and_add_to_list(file_location):
    numbers_list = []

    with open(file_location) as open_file:
        line_in_file = open_file.readline()
        while line_in_file:
            numbers_list.append(line_in_file)
            line_in_file = open_file.readline()

    return numbers_list


if __name__ == '__main__':
    main()