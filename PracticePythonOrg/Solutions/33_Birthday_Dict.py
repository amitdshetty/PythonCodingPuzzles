"""
Problem Statement
This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name.
Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and
return the birthday of that person back to them. The interaction should look something like this:

Happy coding!
"""
def main():
    birthday_dict = {}
    birthday_dict['Amit Shetty'] = '01/01/1991'
    birthday_dict['Amrita Sharma'] = '02/02/1992'
    birthday_dict['Amrit Shagun'] = '03/03/1993'
    birthday_dict['Anut Shana'] = '04/04/1994'
    # print(birthday_dict)

    print("Welcome to the birthday dictionary. We know the birthdays of:\n")
    for i in birthday_dict.keys():
        print(i)

    name_to_check = input("Who's birthday do you want to look up?\n").strip()
    if name_to_check in birthday_dict.keys():
        print("{}'s birthday is on {}".format(name_to_check, birthday_dict[name_to_check]))
    else:
        print('Name entered does not match any records. Enter the full name as shown earlier.')

if __name__ == '__main__':
    main()