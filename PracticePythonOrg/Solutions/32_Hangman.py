import random
import numpy

def main():
    initialize_hangman_game()


def initialize_hangman_game():
    word_to_guess = generate_hangman_word()
    length_of_string = len(word_to_guess)
    hangman_list = []
    for i in range(length_of_string):
        hangman_list.append("_")
    print("".join(hangman_list))
    play_count = 0
    incorrect_guesses = 6
    # Printing for the sake of it. Actual game this won't be needed
    print("The word to guess is {}".format(word_to_guess))
    guesses_made_so_far = set()
    play_hangman(hangman_list, word_to_guess, play_count, incorrect_guesses, guesses_made_so_far)


def play_hangman(hangman_list, word_to_guess, play_count, incorrect_guesses, guesses_made_so_far):
    """
    This method is used recursively to fill the blank in the hangman list until all the blanks are filled
    :param hangman_list: list shown to the user that fills as the user keeps making guesses
    :param word_to_guess: Comopter generated word that user needs to guess
    :param play_count: Records how many times user has made a guess
    :param incorrect_guesses: Records how many chances re left for the player to make a guess
    """
    # Based on game rules if number of incorrect guesses reaches 0. Game is Over
    if incorrect_guesses == 0:
        print("You have used all your guesses. You lose.\nTime to play again")
        initialize_hangman_game()
    else:
        user_guess = input(
            "Please enter a guess. You have {} blanks to fill and have {} incorrect guesses left\n".format(
                hangman_list.count("_"), incorrect_guesses))
        match_index = []
        # User input validation so that only upper case values are compared
        if user_guess != "" and len(user_guess.strip()) == 1:
            user_guess = user_guess.upper()
            play_count = play_count + 1
            # Check if user input is somethign the user already guessed before else proceed with game
            # Also check if user has made  aduplicate guess. Purpose is not penalise them
            if user_guess in hangman_list or user_guess in guesses_made_so_far :
                print("This has already been guessed. Try again")
                guesses_made_so_far.add(user_guess)
                play_hangman(hangman_list, word_to_guess, play_count, incorrect_guesses, guesses_made_so_far)
            else:
                guesses_made_so_far.add(user_guess)
                if user_guess in word_to_guess:
                    for index, word in enumerate(word_to_guess):
                        if user_guess == word:
                            # Index to fill the words into the hangman list that is shown to the user
                            match_index.append(index)
                else:
                    incorrect_guesses = incorrect_guesses - 1
                    print("This word does not match any blank. Try again\n")
                    play_hangman(hangman_list, word_to_guess, play_count, incorrect_guesses, guesses_made_so_far)
            # This loop replaces the blanks in the hangman list with the correct user guesses
            for i in match_index:
                hangman_list[i] = user_guess
            print("".join(hangman_list))
            # If there is still a blank left in hangman_list, game continues else it ends
            if "_" in hangman_list:
                play_hangman(hangman_list, word_to_guess, play_count, incorrect_guesses, guesses_made_so_far)
            else:
                print("Game Over. Youn won. It took {} counts\nTime to play again".format(play_count))
                initialize_hangman_game()
        else:
            print("User input is valid. Please try again\n")
            play_hangman(hangman_list, word_to_guess, play_count, incorrect_guesses, guesses_made_so_far)

def generate_hangman_word():
    file_dir = "/Users/amitshetty/Desktop/Projects/PracticePythonFiles/30 _Pick_Word"
    file_name = "SOWPODS.txt"
    with open(file_dir + "/" + file_name, "r") as lines:
        line = lines.readlines()
        # Using numpy random function
        # word = np.random.choice(line, 1)
        word = random.sample(line, 1)
    return word[0].strip()

if __name__ == '__main__':
    main()