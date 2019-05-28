"""
Problem Statement

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

"""

def main():
    keepPlaying = True
    validMoves = [1, 2, 3]
    theQuestion = 'What is your move? Select from the options below\n1.Rock\n2.Paper\n3.Scissors'
    while keepPlaying :
        print('Player 1, ' + theQuestion)

        inputbyPlayer1 = int(input())
        print('Player 1, you chose ' + str(inputbyPlayer1))
        if inputbyPlayer1 not in validMoves :
            print('Player 1, invalid move. Try again')
            continue
        print('Player 2, ' + theQuestion)

        inputbyPlayer2 = int(input())
        print('Player 2, you chose ' + str(inputbyPlayer2))
        if inputbyPlayer2 not in validMoves :
            print('Player 2, invalid move. Try again')
            continue
        """
        This dictionary basically translates to 
        movesThatCanBeatYourMove = { Rock is beaten by paper, Paper is beaten by scissors, Scissors is beaten by rock }
        """
        movesThatCanBeatYourMove = {1: 2, 2: 3, 3: 1}
        if inputbyPlayer1 == inputbyPlayer2:
            print("You have entered the same moves. It's a tie. Try again.")
            continue
        else:
            if movesThatCanBeatYourMove[inputbyPlayer1] == inputbyPlayer2:
                print('Player 2 wins')
                keepPlaying = False
            elif movesThatCanBeatYourMove[inputbyPlayer2] == inputbyPlayer1:
                print('Player 1 wins')
                keepPlaying = False


if __name__ == '__main__':
    main()