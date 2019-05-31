"""
Problem Statement
This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1
to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on
disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting
bigger and bigger.
"""
import json
import os
import stat

file_name = '/Users/amitshetty/Desktop/birthday_json.json'

def main():
    read_and_update_json()

def check_if_file_empty():
    """
    This is needed since the the open() method raises an error if file is empty
    :return: True if file is not empty else False
    """
    if os.stat(file_name)[stat.ST_SIZE] == 0:
        return False
    return True

def read_and_update_json():
    try:
        if check_if_file_empty():
            with open(file_name, 'r', encoding='UTF-8') as file_read:
                birthday_dict = json.load(file_read)
                # print(birthday_dict)
                if len(birthday_dict) > 0:
                    print('Welcome to the birthday dictionary. The following birthdays are known')
                    for i in birthday_dict.keys():
                        print("{}'s birthday is {}".format(i, birthday_dict[i]))
                    print('Would you like to add a name and birthday to the file? Leave blank if not needed')
                    name = input("Name: ")
                    birthday = input("Birthday: ")
                    if not name or not birthday:
                        print("No user added to file.")
                    else:
                        with open(file_name, 'w') as file_write:
                            birthday_dict.update({name: birthday})
                            json.dump(birthday_dict, file_write)
                else:
                    print('No data is file.\n')
        else:
            print('File is empty. Writing default values to file. Loading application again.')
            write_to_json()
            read_and_update_json()
    except ValueError as vError:
        print(vError)
    except IOError as ioError:
        print(ioError)


def write_to_json():
    """
    Write to file. Inefficient since it repeats every single time the process of writing to file
    JSON however is not a very good option for file storage
    Refer: https://stackoverflow.com/questions/12994442/how-to-append-data-to-a-json-file
    :return:
    """
    birthday_dict = {}
    birthday_dict['Amit Shetty'] = '01/01/1991'
    birthday_dict['Amrita Sharma'] = '02/02/1992'
    birthday_dict['Amrit Shagun'] = '03/03/1993'
    birthday_dict['Anut Shana'] = '04/04/1994'

    with open(file_name, 'w') as file_json:
        json.dump(birthday_dict, file_json)

if __name__ == '__main__':
    main()