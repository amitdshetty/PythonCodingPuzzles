"""
Problem Statements
This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""
import os
import stat
import json

file_name = '/Users/amitshetty/Desktop/birthday_json.json'

def main():
    prepare_month_dictionary()


def prepare_month_dictionary():
    if check_if_file_empty():
        # Apply logic to load json and split the data base don the '/' and extract month
        with open(file_name, 'r') as file_read:
            month_dictionary = {
                "01": "January",
                "02": "February",
                "03": "March",
                "04": "April",
                "05": "May",
                "06": "June",
                "07": "July",
                "08": "August",
                "09": "September",
                "10": "October",
                "11": "November",
                "12": "December"
            }
            birthday_dict = json.load(file_read)
            month_list = []
            for k, v in birthday_dict.items():
                month_birthday = v.split('/')
                # Month is the second element in the date assuming
                month_list.append(month_birthday[1])
            # Get unique elements from the list to create a smaller loop for counting the number of occurences in the list
            month_set = set(month_list)
            final_dict = {}
            for k in month_set:
                count = month_list.count(k)
                final_dict[month_dictionary[k]] = count
            final_dict_sorted = {}
            # Useful method to sort a dictionary by value and return a dictionary
            for key, value in sorted(final_dict.items(), key=lambda x: x[1], reverse=True):
                final_dict_sorted[key] = value
            print(final_dict_sorted)


def check_if_file_empty():
    """
    This is needed since the the open() method raises an error if file is empty
    :return: True if file is not empty else False
    """
    if os.stat(file_name)[stat.ST_SIZE] == 0:
        return False
    return True

if __name__ == '__main__':
    main()