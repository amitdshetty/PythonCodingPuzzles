"""
Problem Statement
This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary
of words used in professional Scrabble tournaments. Each line in the file contains a single word.
"""
import numpy as np
import random
def main():
    file_dir = "/Users/amitshetty/Desktop/Projects/PracticePythonFiles/30 _Pick_Word"
    file_name = "SOWPODS.txt"
    with open(file_dir + "/" + file_name, "r") as lines:
        line = lines.readlines()
        # Using numpy random function
        #word = np.random.choice(line, 1)
        word = random.sample(line, 1)
    print(word[0])


if __name__ == '__main__':
    main()