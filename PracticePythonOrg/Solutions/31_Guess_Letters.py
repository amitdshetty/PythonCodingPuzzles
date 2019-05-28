"""
Problem Statement
This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters
incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and
displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get
the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess
that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly
or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.
"""

def main():
    word_to_guess = "EVAPORATE"
    length_of_string = len(word_to_guess)
    hangman_list = []
    for i in range(length_of_string):
        hangman_list.append("_")
    print("".join(hangman_list))
    play_count = 0
    play_hangman(hangman_list, word_to_guess, play_count)


def play_hangman(hangman_list, word_to_guess, play_count):
    """
    This method is used recursively to fill the blank in the hangman list until all the blanks are filled
    :param hangman_list: list shown to the user that fills as the user keeps making guesses
    :param word_to_guess: Comopter generated word that user needs to guess
    :param play_count: Records how many times user has made a guess
    """
    user_guess = input("Please enter a guess. You have {} blanks to fill\n".format(hangman_list.count("_")))
    match_index = []
    # User input validation so that only upper case values are compared
    if user_guess != "" and len(user_guess.strip()) == 1:
        user_guess = user_guess.upper()
        play_count = play_count + 1
        if user_guess in hangman_list:
            print("This has already been guessed. Try again")
            play_hangman(hangman_list, word_to_guess, play_count)
        else:
            if user_guess in word_to_guess:
                for index, word in enumerate(word_to_guess):
                    if user_guess == word:
                        # Index to fir the words into the hangman list that is shown to the user
                        match_index.append(index)
            else:
                print("This word does not match any blank. Try again\n")
                play_hangman(hangman_list, word_to_guess, play_count)
        # This loop replaces the blanks in the hangman list with the correct user guesses
        for i in match_index:
            hangman_list[i] = user_guess
        print("".join(hangman_list))
        # If there is still a blank left in hangman_list, game continues else it ends
        if "_" in hangman_list:
            play_hangman(hangman_list, word_to_guess, play_count)
        else:
            print("Game Over. It took {} counts".format(play_count))
    else:
        print("User input is valid. Please try again\n")
        play_hangman(hangman_list, word_to_guess, play_count)


if __name__ == '__main__':
    main()
