"""
Problem Statement

Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and
if statements!
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
            if check_for_win(board_state):
                # Assigning minus 1 so that the draw condition is not satisfied.
                # This is case the game is decided in the last box
                play_game(-1 , board_state)
            else:
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
            if check_for_win(board_state):
                # Assigning minus 1 so that the draw condition is not satisfied.
                # This is case the game is decided in the last box
                play_game(-1, board_state)
            else:
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
# TBD: For some reason code cannot be importted from another file


"""
For key 8 we directly print the message that no winner is found instead of no winner found at second diagonal since 
there is no other path for the application to follow
"""
message_dict = {
    1: "Vertical Winner is {}",
    2: "Horizontal Winner is {}",
    3: "First diagonal winner is {}",
    4: "Second diagonal winner is {}",
    5: "No winner found vertically",
    6: "No winner found horizontally",
    7: "No winner found in the first diagonal",
    8: "No winner found"
}

"""
Both lists correspond to the keys in the dictionary declared above
"""
valid_win_cases = [1, 2, 3, 4]
valid_loss_cases = [5, 6, 7, 8]


def check_for_win(current_state_of_board):
    for i in range(1):
        temp_check, a = check_vertical(current_state_of_board)
        if first_come_first_serve(a, temp_check):
            break
        temp_check, a = check_horizontal(current_state_of_board)
        if first_come_first_serve(a, temp_check):
            break
        temp_check, a = check_first_diagonal(current_state_of_board)
        if first_come_first_serve(a, temp_check):
            break
        temp_check, a = check_second_diagonal(current_state_of_board)
        if first_come_first_serve(a, temp_check):
            break
    smart_print(a, temp_check)
    return True if a in valid_win_cases else False

def first_come_first_serve(a, temp_check):
    """
    Determines break condition to stop the program if it already find a winner
    :param a:
    :param temp_check:
    :return:
    """
    return True if a in valid_win_cases else False


def smart_print(a, temp_check):
    """
    Function prints statements for each win and loss based on a message dictionary
    Purpose is to give user specific messages without adding too many conditions
    :param a:
    :param temp_check:
    :return:
    """
    if a in valid_win_cases:
        """
        Note: It was possible to just write 

            temp_list = list(temp_check)
            temp_list.get(0)

        in order to avoid popping the element altogether. It is not needed in this case because:
        1. No need to create a new list
        2. Temp_check as the name suggests is not needed once element is retrieved
        """
        print(message_dict.get(a).format(temp_check.pop()))
    elif a in valid_loss_cases:
        print(message_dict.get(8))


def check_second_diagonal(current_state_of_board):
    # Check to see if the right hand diagonal elements match up
    temp_second_diag_check = []
    for i in range(3):
        for j in range(3):
            if i + j == len(current_state_of_board[0]) - 1:
                temp_second_diag_check.append(current_state_of_board[i][j])
    temp_check = set(temp_second_diag_check)
    a = 4 if len(temp_check) == 1 and list(temp_check)[0] != 0 else 8
    return temp_check, a


def check_first_diagonal(current_state_of_board):
    # Check to see if the left hand diagonal elements match up
    a = 0
    temp_first_diag_check = []
    for i in range(3):
        for j in range(3):
            if i == j:
                temp_first_diag_check.append(current_state_of_board[i][j])
    temp_check = set(temp_first_diag_check)
    a = 3 if len(temp_check) == 1 and list(temp_check)[0] != 0 else 7
    return temp_check, a


def check_vertical(current_state_of_board):
    # Check to see if the columns in the list of lists have the same number i.e. Vertical Check
    a = 0
    for i in range(3):
        temp_vertical_check = []
        for j in range(3):
            temp_vertical_check.append(current_state_of_board[j][i])
        temp_check = set(temp_vertical_check)
        if len(temp_check) == 1 and list(temp_check)[0] != 0:
            a = 1
            break
        else:
            a = 5
    return temp_check, a


def check_horizontal(current_state_of_board):
    # Check each list to see if they have the same number i.e. Horizontal Check
    a = 0
    for i in range(3):
        temp_check = set(current_state_of_board[i])
        """
        Note that 0 indicates a blank space and is therefore not considered when deciding a winner
        i.e. 0 cannot be a winner
        """
        if len(temp_check) == 1 and list(temp_check)[0] != 0:
            a = 2
            break
        else:
            a = 6
    return temp_check, a


if __name__ == '__main__':
    main()