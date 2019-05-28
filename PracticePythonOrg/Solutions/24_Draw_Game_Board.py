"""
Problem Statement:
This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
"""

def main():
    board_draw(3,3)
    board_draw_jugaad(3,3)

def board_draw(height, width):
    """
    Only problem with this method is that board only 95% uniform
    :param height:
    :param width:
    :return:
    """
    print("Board without jugaad => ")
    print(" --- " * width)
    for x in range(height):
        a = "|    "
        #width = width-1
        #print(a * width if x < height else '|')
        print(a * width,end='')
        print("\b|")
        print(" --- " * width)

def board_draw_jugaad(heigth, width):
    """
    This is a hundred percent uniform except that there are 2 bars in the mniddle for the checkers game
    :param heigth:
    :param width:
    :return:
    """
    print("Board with jugaad => ")
    print(" --- "*width)
    for x in range(heigth):
        print("|   |" * width)
        print(" --- " * width)



if __name__ == '__main__':
    main()