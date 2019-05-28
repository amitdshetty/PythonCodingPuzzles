"""
Problem Statement
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and
if statements!
"""
def main():
  user_input = [11, 43, 9]
  max = 0
  for i in user_input:
    if i > max:
      max = i
  print("Maximum is {}".format(max))

if __name__ == '__main__':
    main()