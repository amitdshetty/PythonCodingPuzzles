"""
Problem Statement

Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are.
This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit
about string parsing in Python 3. I talked a little bit about it in this post.
"""

def main():
    file_location_1 = '/Users/amitshetty/Desktop/nameslist.txt'
    file_location_2 = '/Users/amitshetty/Desktop/Training_01.txt'
    try:
        challenge_1(file_location_1)
        challenge_2(file_location_2)
    except FileNotFoundError as fnferr:
        print('Invalid File Location',fnferr)
    else:
        print('So this just happened')
    finally:
        print('Program Ends')


def challenge_2(file_location):
    """
    Print the categories from a large text file of image locations
    :param file_location:
    :return:
    """
    categories_list = []
    with open(file_location, 'r') as open_file:
        line_in_file = open_file.readline()
        while line_in_file:
            strings = line_in_file.split('/')
            # Section of the link that contains then category
            categories_list.append(strings[2])
            line_in_file = open_file.readline()
    print("The length of the list is {list_length}".format(list_length=len(categories_list)))
    # Set ensures unique categories can be isolates as there is not previous knowledge of what possible categories are given to us
    categories_set = set(categories_list)
    #print("categories_set = {this_set}".format(this_set=categories_set))
    final_result_dict = {}
    for category in categories_set:
        # print("{catagry} appears {no_of_times} times".format(catagry = category, no_of_times = categories_list.count(category)))
        final_result_dict[category] = categories_list.count(category)
    print('Category => Count')
    for cat, count_cat in final_result_dict.items():
        print("{} => {}".format(cat, count_cat))


def challenge_1(file_location):
    """
    Simple file reading to print 2 lines
    :param file_location:
    :return:
    """
    with open(file_location, 'r') as open_file:
        line_in_file = open_file.readline()
        while line_in_file:
            print(line_in_file)
            line_in_file = open_file.readline()


if __name__ == '__main__':
    main()