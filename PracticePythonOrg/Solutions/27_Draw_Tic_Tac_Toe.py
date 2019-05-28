"""
Problem Statement
This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game.
In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2
(or whoever is X and O won).
"""

def main():
    board_state = [[0,0,0],
                   [0,0,0],
                   [0,0,0]]
    """
    Validate input by user
    At the beginning of each move check if the any one has won
    """
    print_board_state(board_state)
    turn = 1
    play_game(turn, board_state)


def play_game(turn, board_state):
    """
    Use turn variable to determine who's turn it is to play
    Turn = 1 or 2 imlies player1 or player 2 playing
    Turn = 0 implies the all boxes have been filled and no winner has been determined
    Turn = -1 imlies that the game is over with winner chosen
    :param turn:
    :param board_state:
    :return:
    """
    if turn == -1:
        print('Game Over.')
    if is_game_over(board_state):
        print('No more moves possible.It is a draw')
        # Override turn variable so that game does not proceed further
        turn = 0
    if turn == 1:
        player1 = input('Player 1: Your move? Enter in format <row><space><column>\n')
        player1_x, player1_y = clean_input(player1)
        if check_if_valid_move(board_state, player1_x, player1_y):
            board_state[player1_x][player1_y] = 1
            print_board_state(board_state)
            play_game(2, board_state)
        else:
            print('Invalid Move. Try again')
            print_board_state(board_state)
            play_game(1, board_state)

    if turn == 2:
        player2 = input('Player 2: Your move? Enter in format <row><space><column>\n')
        player2_x, player2_y = clean_input(player2)
        if check_if_valid_move(board_state, player2_x, player2_y):
            board_state[player2_x][player2_y] = 2
            print_board_state(board_state)
            play_game(1, board_state)
        else:
            print('Invalid Move. Try again')
            print_board_state(board_state)
            play_game(2, board_state)


def is_game_over(board):
    # Check if all the cells are populated. If true game over with no winner
    for brd in board:
        if 0 in brd:
            return False
    return True

def check_if_valid_move(board, x, y):
    # If a box has already been filled then a move to that box is invalid
    if board[x][y] == 0:
        return True
    return False


def print_board_state(current_board_state):
    for row in current_board_state:
        print(row, end = '\n')

def clean_input(playerInput):
    # Splitting the input into row and column co-ordinate and taking out the whitespace
    if playerInput == '':
        return None
    x, y = playerInput.split()
    x.strip()
    y.strip()
    return int(x), int(y)

# Board Calculation using code from previous exercise
# TBD: For some reason code cannot be imported from another file


"""
For key 8 we directly print the message that no winner is found instead of no winner found at second diagonal since 
there is no other path for the application to follow
"""

if __name__ == '__main__':
    main()