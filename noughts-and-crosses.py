from random import randrange


board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]]


def display_board(board):
    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """
    print(
        f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
"""
    )


def enter_move(board):
    """
    The function accepts the board's current status, asks the user about their move,
    checks the input, and updates the board according to the user's decision.
    """
    options = make_list_of_free_fields(board)
    num_options = [board[option[0]][option[1]] for option in options]
    user = None

    while user == None:
        try:
            user = int(input('Make your move: '))
        except ValueError:
            user = None
            print("That's not a number! Please pick a number 1-9")
        else:
            if user not in num_options:
                user = None
                print('Invalid number, please pick a number 1-9 that has not been taken')

    # Adjust user to 0 indexing, and then use floor division and modulo against column length (len(board[0])).
    # This technique is effective for any matrix shape.
    row = (user - 1) // 3
    column = (user - 1) % 3
    board[row][column] = 'O'


def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares;
    the list consists of tuples, while each tuple is a pair of row and column numbers.
    """
    return [(row, column) for row in range(3) for column in range(3) if board[row][column] not in ['O', 'X']]


def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if
    the player using 'O's or 'X's has won the game
    """
    for i in range(3):
        col = [board[j][i] for j in range(3)]
        board.append(col)

    diag_1 = [board[0][0], board[1][1], board[2][2]]
    diag_2 = [board[0][2], board[1][1], board[2][0]]

    board.append(diag_1)
    board.append(diag_2)

    for line in board:
        if line.count(sign) == 3:
            return True
    return False


def draw_move(board):
    """
    The function draws the computer's move and updates the board.
    """
    options = make_list_of_free_fields(board)
    choice = options[randrange(len(options))]

    board[choice[0]][choice[1]] = 'X'


def main(board):
    """
    The function runs the game. Prints game outcome message to the terminal.
    """
    while len(make_list_of_free_fields(board)):
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            break
        display_board(board)
        draw_move(board)
        if victory_for(board, 'X'):
            break

    display_board(board)

    if victory_for(board, 'X'):
        print('Loser! 😢')
    elif len(make_list_of_free_fields(board)) == 0:
        print("No more moves, it's a draw. 😐")
    else:
        print('Winner! 😁')


main(board)
