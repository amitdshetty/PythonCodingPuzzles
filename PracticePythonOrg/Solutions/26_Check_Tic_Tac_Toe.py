"""
Problem Statement

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any.
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every
board there will only be one winner.
"""

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

def main():
    current_state_of_board1 = [[1, 2, 0],
                              [2, 1, 0],
                              [2, 1, 1]]

    current_state_of_board2 = [[2, 2, 0],
                              [2, 1, 0],
                              [2, 1, 1]]

    current_state_of_board3 = [[1, 2, 0],
                              [2, 1, 0],
                              [2, 1, 1]]

    current_state_of_board4 = [[0, 1, 0],
                              [2, 1, 0],
                              [2, 1, 1]]

    current_state_of_board5 = [[1, 2, 0],
                              [2, 1, 0],
                              [2, 1, 2]]

    current_state_of_board = [[1, 2, 0],
                              [2, 1, 0],
                              [2, 1, 0]]

    """
    For loop with a single loop cycle to ensure it is easy to break out of the loop if a winner is found using 
    one of the techniques
    """
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
        print(message_dict.get(a))


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